from comments.models import Comment
from replies.models import Reply
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ReplySerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def display_replies(request,pk):
    comment = Comment.objects.get(id=pk)
    if request.method == 'GET':
        replies = Reply.objects.filter(comment=comment)
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, comment_id=pk)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def post_reply_to_video(request):