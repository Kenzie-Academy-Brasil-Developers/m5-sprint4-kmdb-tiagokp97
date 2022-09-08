from django.shortcuts import get_object_or_404
from movie.models import Movie
from movie.serializer import MovieSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Request, Response, status

from review.models import Review
from review.serializers import ReviewSerializer

from .models import Review
from .permissions import IsAdminOrCritic, IsAdminOrReadOnly


class ReviewView(APIView, PageNumberPagination):
  def get(self, request: Request, movie_id:int) -> Response:
    reviews = Review.objects.filter(movie_id=movie_id)
    
    result_page = self.paginate_queryset(reviews, request, view=self)
    
    serializer = ReviewSerializer(result_page, many=True)

    return self.get_paginated_response(serializer.data)
  
  def post(self, request: Request, movie_id:int) -> Response:
    movie:Movie = get_object_or_404(Movie, id=movie_id)

    review_already_exists = Review.objects.filter(movie_id=movie.id, critic_id=request.user.id).exists()

    if review_already_exists:
      return Response({"detail": "Review already exists."}, status.HTTP_400_BAD_REQUEST)

    serializer = ReviewSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)

    serializer.save(movie=movie, critic=request.user)

    return Response(serializer.data, status.HTTP_201_CREATED)

class ReviewDetailView(APIView):
  permission_classes = [IsAdminOrCritic, IsAdminOrReadOnly]

  def get(self, request: Request, movie_id:int, review_id:int) -> Response:
    reviews:Review = Review.objects.filter(movie_id=movie_id)
    
    review = [review for review in reviews if review.id == review_id ]
    
    serializer = ReviewSerializer(review[0])

    return Response(serializer.data, status.HTTP_200_OK)
  
  def delete(self, request: Request, movie_id:int, review_id:int):
    reviews:Review = Review.objects.filter(movie_id=movie_id)
    
    review = [review for review in reviews if review.id == review_id ]

    self.check_object_permissions(request, request.user)

    review[0].delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)
