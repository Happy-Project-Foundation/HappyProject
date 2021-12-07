from typing import Any, Dict

from django.views.generic import TemplateView

from home.models import FAQ


# Utility Classes ------------------------------------------------------------

class Offers(object):
    def __init__(self, title: str, icon: str, text: str) -> None:
        self.title = title
        self.text = text
        self.icon = icon


class HowToItem(object):
    def __init__(self, title: str, icon: str, text: str) -> None:
        self.title = title
        self.text = text
        self.icon = icon


# Generic Views --------------------------------------------------------------

class HomeView(TemplateView):
    template_name = "home/index.html"

    # Offers for the offer section
    _offers = [
        Offers(
            title="Abundant of Exam Papers",
            text="We offer variety of past papers, pilot exams, model papers for free." +
            " We accomplish by indexing exam papers in the internet and offer them at your ease for free-of-charge",
            icon="copy"
        ),
        Offers(
            title="Plenty of Tutorials",
            text="Happy Project also offers plenty of tutorials by indexing them and making them at your ease. All the tutorials we offer are free-of-charge and reviewed before exposure to general public, so that you can learn from the best that is correct in sense!",
            icon="sticky-note"
        ),
        Offers(
            title="A Happy Pool of Thoughts",
            text="Happy Project also exposes you to a community of non-profit humans around the globe to help you or get help from you. This is a Happy Community",
            icon="lightbulb-on"
        ),
        Offers(
            title="Generous Happy Scholarships",
            text="Happy exposes you to happyScholarships that are offered by third-party in a non-profit goal and WE(Happy Project) acts as an agent in between two parties!",
            icon="graduation-cap"
        ),
    ]

    # HowToItems for the how_to section
    _howtos = [
        HowToItem(
            title="IF you == Student:",
            text="You can use Happy Project to GET ♾️ access to ocean of exam papers, tutorials, scholarships and a community to voice yourself.",
            icon="book-reader"
        ), 
        HowToItem(
            title="IF you == Teacher:",
            text="You can be use Happy Project to GIVE what you have to the Happy Community and this Happy Project a much more resourcesful one🤗.",
            icon="chalkboard-teacher"
        ),
        HowToItem(
            title="IF you == Donor:",
            text="You can use Happy Project to show your generous mind by either issusing scholarships to those who need or sponsor the developemnt and maintenance of Happy Project.",
            icon="award"
        ),
        HowToItem(
            title="IF you == Technician:",
            text="You can guide Happy Project technically and make this THING going forward without any technical issues. If you are then guide us via E-mail, Twitter etc.",
            icon="cogs"
        ),
        HowToItem(
            title="IF you == Developer:",
            text="You can either use or help Happy Project by becoming a contributor for the source text. If you are then fork(🍴) and PR us your work.",
            icon="code"
        ),
        HowToItem(
            title="IF you == Anyone:",
            text="Please share the words to those who might make use of Happy Project and help us keep Happy Project alive by becoming someone among above!",
            icon="user-astronaut"
        ),
    ]

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        
        # retrieval of super context
        context = super().get_context_data(**kwargs)
        
        # offers compilation
        context["offers"] = self._offers
        
        # howtos compilation
        context["howtos"] = self._howtos

        # retrival and compilation of FAQs
        faqs = FAQ.objects.all()[:10]
        context["faqs"] = faqs

        return context