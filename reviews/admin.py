from django.contrib import admin
from .models import Movie, Review


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "genre",
        "release_date",
        "avg_rating_display",
        "review_count_display",
    )
    list_filter = ("genre", "release_date")
    search_fields = ("title", "tagline", "description", "genre")
    ordering = ("-release_date", "title")
    date_hierarchy = "release_date"

    @admin.display(description="Avg rating")
    def avg_rating_display(self, obj):
        return f"{obj.avg_rating:.1f}"

    @admin.display(description="Reviews")
    def review_count_display(self, obj):
        return obj.review_count


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("movie", "name", "rating", "short_comment", "created_at")
    list_filter = ("rating", "created_at", "movie")
    search_fields = ("movie__title", "name", "comment")
    ordering = ("-created_at",)

    def short_comment(self, obj):
        text = obj.comment or ""
        return (text[:60] + "…") if len(text) > 60 else text

    short_comment.short_description = "Comment"
