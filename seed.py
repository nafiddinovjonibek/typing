import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from home.models import Text

texts = [
    {
        'title': 'Salom Dunyo',
        'content': 'Dasturlash dunyosiga xush kelibsiz. Har bir dasturchi o\'z yo\'lini birinchi qadamdan boshlaydi. Bugun siz ham yangi narsalarni o\'rganasiz.',
        'difficulty': 'easy',
    },
    {
        'title': 'Python haqida',
        'content': 'Python zamonaviy dasturlash tillaridan biri hisoblanadi. U sodda sintaksisi va kuchli kutubxonalari bilan mashhur. Python yordamida veb ilovalar, sun\'iy intellekt va ma\'lumotlar tahlili bilan shug\'ullanish mumkin.',
        'difficulty': 'medium',
    },
    {
        'title': 'Tezkor yozish',
        'content': 'Tezkor yozish ko\'nikmasi zamonaviy dunyoda juda muhim hisoblanadi. Kompyuterda ishlash samaradorligini oshirish uchun klaviaturada tez va aniq yozishni o\'rganish kerak. Har kuni mashq qilish orqali siz o\'z tezligingizni sezilarli darajada oshirishingiz mumkin.',
        'difficulty': 'medium',
    },
    {
        'title': 'Django framework',
        'content': 'Django Python dasturlash tilida yozilgan bepul va ochiq kodli veb framework hisoblanadi. U model-template-view arxitektura naqshiga amal qiladi. Django xavfsizlik, kengayuvchanlik va tezkor rivojlantirish imkoniyatlarini taqdim etadi. Ko\'plab mashhur veb saytlar Django asosida qurilgan.',
        'difficulty': 'hard',
    },
]

for t in texts:
    Text.objects.get_or_create(title=t['title'], defaults=t)
    print(f"+ {t['title']}")

print("Tayyor!")
