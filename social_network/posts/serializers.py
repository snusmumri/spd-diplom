from rest_framework import serializers

from posts.models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'comment_text', 'created_at',)
        #read_only_fields = ('user', )


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('like', 'user', 'posts')

# class PostSerializer(serializers.ModelSerializer):
#     comments = CommentSerializer(many=True, read_only=True)
#     likes_count = LikeSerializer(many=True, read_only=True)
#
#     #serializers.SerializerMethodField()
#     class Meta:
#         model = Post
#         fields = ('id', 'user', 'post_text', 'image', 'created_at', 'comments', 'likes_count')
#         read_only_fields = ('user',)
#
#     def likes_count(self, posts):
#         likes_count = Like.objects.filter(post_id=posts.id).count()
#         return likes_count


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'user', 'post_text', 'image', 'created_at', 'comments', 'likes_count')
        read_only_fields = ('user',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        likes_count = Like.objects.filter(post=instance).count()
        representation['likes_count'] = likes_count

        return representation
