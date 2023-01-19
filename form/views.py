from django.shortcuts import render

from form.forms import FeedBackForm


def render_form_view(request):
    return render(request, 'main/form.html')


def save_form_view(request):
    feed_back_form = FeedBackForm(request.POST, request.FILES)
    if feed_back_form.is_valid():
        feed_back_form.save()
        context = {
            'alert_class': 'alert-success',
            'title': f"Спасибо за ваш отзыв: {feed_back_form.cleaned_data['email']}",

            'description': """
            Большое спасибо за замечательный отзыв и внимание к нашей работе. Мы очень ценим, что у нас есть такие отзывчивые клиенты, как вы. Непременно передадим ваши добрые слова нашему коллективу! Ждём вас в гости снова!
            """,
            "footer": 'С наилучшими пожеланиями, администрация приложение такси Za-Kaz'
        }

        return render(request, 'components/message.html', context=context)
    else:
        context = {
            'alert_class': 'alert-danger',
            'title': f"Что то пошло не так",

            'description': """
                    """,
            "footer": ''
        }
        return render(request, 'components/message.html', context=context)
