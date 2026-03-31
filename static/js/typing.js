const textDisplay = document.getElementById('textDisplay');
const typingInput = document.getElementById('typingInput');
const timerEl = document.getElementById('timer');
const wpmEl = document.getElementById('wpm');
const accuracyEl = document.getElementById('accuracy');
const resultPanel = document.getElementById('resultPanel');

let startTime = null;
let timerInterval = null;
let finished = false;

// Render characters
function renderText() {
    textDisplay.innerHTML = '';
    for (let i = 0; i < originalText.length; i++) {
        const span = document.createElement('span');
        span.className = 'char';
        span.textContent = originalText[i];
        if (i === 0) span.classList.add('current');
        textDisplay.appendChild(span);
    }
}

function updateDisplay(typed) {
    const chars = textDisplay.querySelectorAll('.char');
    let correctCount = 0;

    for (let i = 0; i < originalText.length; i++) {
        chars[i].className = 'char';
        if (i < typed.length) {
            if (typed[i] === originalText[i]) {
                chars[i].classList.add('correct');
                correctCount++;
            } else {
                chars[i].classList.add('incorrect');
            }
        } else if (i === typed.length) {
            chars[i].classList.add('current');
        }
    }

    // Scroll current char into view
    const currentChar = textDisplay.querySelector('.char.current');
    if (currentChar) {
        currentChar.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    }

    // Calculate stats
    const elapsed = (Date.now() - startTime) / 1000;
    const minutes = elapsed / 60;
    const wordCount = typed.length / 5; // standard: 5 chars = 1 word
    const wpm = minutes > 0 ? Math.round(wordCount / minutes) : 0;
    const accuracy = typed.length > 0 ? Math.round((correctCount / typed.length) * 100) : 100;

    wpmEl.textContent = wpm;
    accuracyEl.textContent = accuracy + '%';

    return { wpm, accuracy, elapsed, correctCount };
}

function startTimer() {
    startTime = Date.now();
    timerInterval = setInterval(() => {
        const elapsed = Math.round((Date.now() - startTime) / 1000);
        timerEl.textContent = elapsed + 's';
    }, 200);
}

function finishTest(stats) {
    finished = true;
    clearInterval(timerInterval);
    typingInput.disabled = true;

    document.getElementById('finalWpm').textContent = stats.wpm;
    document.getElementById('finalAccuracy').textContent = stats.accuracy + '%';
    document.getElementById('finalTime').textContent = stats.elapsed.toFixed(1) + 's';
    resultPanel.style.display = 'block';

    // Save result
    fetch(`/typing/${textId}/save/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({
            wpm: stats.wpm,
            accuracy: stats.accuracy,
            time_taken: parseFloat(stats.elapsed.toFixed(1)),
        }),
    });
}

typingInput.addEventListener('input', () => {
    if (finished) return;

    const typed = typingInput.value;

    if (!startTime && typed.length > 0) {
        startTimer();
    }

    const stats = updateDisplay(typed);

    // Check if done
    if (typed.length >= originalText.length) {
        finishTest(stats);
    }
});

// Prevent paste
typingInput.addEventListener('paste', (e) => e.preventDefault());

function resetTest() {
    finished = false;
    startTime = null;
    clearInterval(timerInterval);
    typingInput.value = '';
    typingInput.disabled = false;
    timerEl.textContent = '0s';
    wpmEl.textContent = '0';
    accuracyEl.textContent = '100%';
    resultPanel.style.display = 'none';
    renderText();
    typingInput.focus();
}

// Init
renderText();
