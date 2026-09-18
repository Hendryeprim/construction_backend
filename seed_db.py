import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from portfolio.models import Category, Project

interior_cat, _ = Category.objects.get_or_create(name='Interior Design')
construction_cat, _ = Category.objects.get_or_create(name='Commercial Construction')

# --- ADDITIONAL INTERIOR PROJECTS ---

Project.objects.get_or_create(
    title='Nordic Minimalist Loft',
    project_type='INTERIOR',
    location='Helsinki, Finland',
    category=interior_cat,
    description='A clean, functional living space inspired by Scandinavian design principles. Features light woods, neutral tones, and abundant natural light.',
    design_concept='Simplistic elegance, emphasizing space and natural materials.',
    status='Completed',
    timeline='4 Months',
    materials_used='Ash Wood, Concrete, Wool'
)

Project.objects.get_or_create(
    title='The Velvet Lounge',
    project_type='INTERIOR',
    location='Paris, France',
    category=interior_cat,
    description='A dark, moody, and ultra-luxurious private lounge setting. Designed for evening entertainment with rich textures and dramatic lighting.',
    design_concept='Opulence and mystery through heavy fabrics and warm low lighting.',
    status='Completed',
    timeline='6 Months',
    materials_used='Velvet, Brass, Dark Oak, Obsidian'
)

Project.objects.get_or_create(
    title='Urban Zen Studio',
    project_type='INTERIOR',
    location='Tokyo, Japan',
    category=interior_cat,
    description='A small but highly efficient urban apartment designed to feel like a retreat from the bustling city outside.',
    design_concept='Wabi-sabi aesthetics meets modern efficiency.',
    status='Completed',
    timeline='3 Months',
    materials_used='Bamboo, Shoji Paper, Slate'
)

Project.objects.get_or_create(
    title='Desert Modern House',
    project_type='INTERIOR',
    location='Palm Springs, USA',
    category=interior_cat,
    description='An airy interior that seamlessly connects with the arid landscape outside, featuring large glass panes and earth-toned decor.',
    design_concept='Mid-century modern revival with a desert palette.',
    status='Ongoing',
    timeline='7 Months',
    materials_used='Terrazzo, Walnut, Leather'
)


# --- ADDITIONAL CONSTRUCTION PROJECTS ---

Project.objects.get_or_create(
    title='Oasis Museum of Art',
    project_type='CONSTRUCTION',
    location='Dubai, UAE',
    category=construction_cat,
    description='A stunning architectural marvel serving as the city\'s new contemporary art hub. The structure features fluid curves resembling desert dunes.',
    design_concept='Parametric design mimicking natural desert formations.',
    status='Ongoing',
    timeline='4 Years',
    materials_used='Titanium, Glass Fiber Reinforced Concrete, Steel'
)

Project.objects.get_or_create(
    title='Echo Valley Bridge',
    project_type='CONSTRUCTION',
    location='Swiss Alps',
    category=construction_cat,
    description='A highly engineered suspension bridge connecting two mountain peaks, prioritizing both structural integrity and minimalist aesthetic.',
    design_concept='Utilitarian minimalism suspended in nature.',
    status='Completed',
    timeline='5 Years',
    materials_used='High-Tensile Steel, Pre-stressed Concrete'
)

Project.objects.get_or_create(
    title='Silicon Hub Campus',
    project_type='CONSTRUCTION',
    location='San Francisco, USA',
    category=construction_cat,
    description='A massive corporate campus for a leading tech company. Designed for sustainability, featuring living roofs and net-zero energy consumption.',
    design_concept='Sustainable biophilic corporate architecture.',
    status='Ongoing',
    timeline='3 Years',
    materials_used='Mass Timber, Low-E Glass, Recycled Steel'
)

Project.objects.get_or_create(
    title='The Obsidian Hotel',
    project_type='CONSTRUCTION',
    location='Reykjavik, Iceland',
    category=construction_cat,
    description='A luxury boutique hotel carved into a cliffside. The exterior is clad in dark materials to blend with the volcanic landscape.',
    design_concept='Brutalist architecture integrated into raw nature.',
    status='Completed',
    timeline='2.5 Years',
    materials_used='Basalt Rock, Corten Steel, Concrete'
)

print("8 additional sample projects seeded successfully.")
