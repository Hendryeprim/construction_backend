import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()
    username = os.environ.get('ADMIN_USERNAME')
    email = os.environ.get('ADMIN_EMAIL', '')
    password = os.environ.get('ADMIN_PASSWORD')

    if not username or not password:
        print("ADMIN_USERNAME or ADMIN_PASSWORD environment variable not set. Skipping automatic superuser creation.")
        return

    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser: {username}")
        # Using create_superuser which handles password hashing
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superuser created successfully.")
    else:
        print(f"Superuser {username} already exists. Skipping creation.")

if __name__ == '__main__':
    create_superuser()
