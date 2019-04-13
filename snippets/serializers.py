from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# serializers.HyperlinkedModelSerializer
# serializers.Serializer
# dataというメンバ変数を持っていて、そこに全てのメンバ変数が格納されている
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(
        choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    # どこでバリデーションすんねんって思ったけど、JSか
    # validated_dataはid=1,title="hoge"とかって感じかな
    # 正直どんなデータ型かよく分からない 辞書型っぽいとは思う
    def create(self, validated_data):
        # s = Snippet(**validated_data)
        # s.save() と同じ
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
