from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Movie, Review


def home(request):
    movies = Movie.objects.all().prefetch_related("reviews")
    return render(request, "index.html", {"movies": movies})


@require_POST
def add_review(request):
    movie_id = request.POST.get("movie_id")
    name = (request.POST.get("name") or "").strip()
    rating = request.POST.get("rating")
    comment = (request.POST.get("comment") or "").strip()

    if not (movie_id and name and rating and comment):
        return JsonResponse(
            {"success": False, "message": "Please fill in all fields."}, status=400
        )

    try:
        rating = int(rating)
    except ValueError:
        return HttpResponseBadRequest("Invalid rating")

    if rating < 1 or rating > 5:
        return JsonResponse(
            {"success": False, "message": "Rating must be between 1 and 5."}, status=400
        )

    movie = get_object_or_404(Movie, pk=movie_id)

    review = Review.objects.create(
        movie=movie,
        name=name,
        rating=rating,
        comment=comment,
        created_at=timezone.now(),
    )

    return JsonResponse(
        {
            "success": True,
            "message": "Review added successfully!",
            "review": {
                "name": review.name,
                "rating": review.rating,
                "comment": review.comment,
                "created_at": review.created_at.strftime("%b %d, %Y • %I:%M %p"),
            },
            "avg_rating": movie.avg_rating,
            "review_count": movie.review_count,
            "movie_id": movie.id,
        }
    )
