from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class LoginForm(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='username',
            field_required='password',
        )
