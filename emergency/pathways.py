from pathway import pathways
from emergency import models

class BookingIn(pathways.PagePathway):
    display_name = 'ED Booking In'
    slug = 'booking'
    steps = (models.Demographics,)

    def save(self, data, user):
        patient = super(BookingIn, self).save(data, user)
        episode = patient.episode_set.last()
        episode.set_tag_names(["triage"], None)
        return patient

    def redirect_url(self, patient):
        return "/#/list/triage"

