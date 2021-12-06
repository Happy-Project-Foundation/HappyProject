from typing import Any, Dict

from django.views.generic import TemplateView


# Utility Classes ------------------------------------------------------------

class Offers(object):
    def __init__(self, heading: str, icon: str, text: str) -> None:
        self.title = heading
        self.text = text
        self.icon = icon


class HowToItem(object):
    def __init__(self) -> None:
        super().__init__()


# Generic Views --------------------------------------------------------------
class HomeView(TemplateView):
    template_name = "home/index.html"

    # Offers for the offer section
    _offers = [
        Offers(
            heading="Abundant of Exam Papers",
            text="We offer variety of past papers, pilot exams, model papers for free." +
            " We accomplish by indexing exam papers in the internet and offer them at your ease for free-of-charge",
            icon="copy"
        ),
        Offers(
            heading="Plenty of Tutorials",
            text="Happy Project also offers plenty of tutorials by indexing them and making them at your ease. All the tutorials we offer are free-of-charge and reviewed before exposure to general public, so that you can learn from the best that is correct in sense!",
            icon="sticky-note"
        ),
        Offers(
            heading="A Happy Pool of Thoughts",
            text="Happy Project also exposes you to a community of non-profit humans around the globe to help you or get help from you. This is a Happy Community",
            icon="lightbulb-on"
        ),
        Offers(
            heading="Generous Happy Scholarships",
            text="Happy exposes you to happyScholarships that are offered by third-party in a non-profit goal and WE(Happy Project) acts as an agent in between two parties!",
            icon="graduation-cap"
        ),
    ]

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["offers"] = self._offers
        return context