import os
from django.apps import AppConfig
from django.db.models.signals import post_migrate

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

    def ready(self):
        # On utilise un signal post_migrate pour s'assurer que les tables existent
        post_migrate.connect(setup_google_auth, sender=self)

def setup_google_auth(sender, **kwargs):
    """
    Configure automatiquement Google Auth à partir du fichier .env
    """
    from django.contrib.sites.models import Site
    from allauth.socialaccount.models import SocialApp
    
    # 1. Configurer le Site (indispensable pour allauth)
    domain = os.getenv('DOMAIN', '127.0.0.1:8000')
    name = os.getenv('SITE_NAME', 'Habit Tracker')
    
    site, _ = Site.objects.get_or_create(id=1)
    site.domain = domain
    site.name = name
    site.save()

    # 2. Créer ou mettre à jour la Social App Google
    client_id = os.getenv('GOOGLE_CLIENT_ID')
    secret = os.getenv('GOOGLE_CLIENT_SECRET')

    if client_id and secret:
        app, created = SocialApp.objects.get_or_create(
            provider='google',
            defaults={
                'name': 'Google Auth',
                'client_id': client_id,
                'secret': secret,
            }
        )
        
        # Si elle existe déjà, on met à jour les clés si elles ont changé dans le .env
        if not created:
            app.client_id = client_id
            app.secret = secret
            app.save()

        # On lie l'application au site par défaut
        app.sites.add(site)
        
        if created:
            print("✓ Google SocialApp configurée automatiquement.")
