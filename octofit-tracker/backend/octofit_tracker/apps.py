from django.apps import AppConfig

class OctofitTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'octofit_tracker'
    
    def ready(self):
        # Ensure management commands are loaded
        import octofit_tracker.management.commands
