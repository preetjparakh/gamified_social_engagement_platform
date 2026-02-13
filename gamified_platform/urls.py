from django.urls import path

urlpatterns = [
    # Accounts
    path('api/accounts/', include('accounts.urls')),

    # Groups
    path('api/groups/', include('groups.urls')),

    # Chat
    path('api/chat/', include('chat.urls')),

    # Games
    path('api/games/', include('games.urls')),

    # Memories
    path('api/memories/', include('memories.urls')),

    # Incentives
    path('api/incentives/', include('incentives.urls')),

    # Notifications
    path('api/notifications/', include('notifications.urls')),

    # Moderation
    path('api/moderation/', include('moderation.urls')),
]