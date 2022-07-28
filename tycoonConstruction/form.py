from django import forms


class CostForm(forms.Form):
    length = forms.IntegerField(label="Length (fts)")
    width = forms.IntegerField(label="width of wall (inchs)")
    height = forms.IntegerField(label="height (fts)")
    no_of_walls = forms.IntegerField(label="no_of_walls")


class Deduction(forms.Form):
    length = forms.IntegerField(label="Length (fts)")
    width = forms.IntegerField(label="width of wall (inchs)")
    height = forms.IntegerField(label="height (fts)")
    no_of_walls = forms.IntegerField(label="no_of_walls")
    total_meter_wall = forms.FloatField(
        label="total_meter_wall (meter cube (m^3))")


class LabourCost(forms.Form):
    length = forms.FloatField(label="Total Length (fts)")
    width = forms.FloatField(label="Total Width (fts)")
    no_days = forms.IntegerField(label="No of Days")


class PillarCollumn(forms.Form):
    c_length = forms.IntegerField(label="Length (inchs)")
    c_width = forms.IntegerField(label="width of wall (inchs)")
    c_height = forms.IntegerField(label="height (fts)")
    c_no_of_walls = forms.IntegerField(label="no_of_walls")


class RccBeam(forms.Form):
    b_length = forms.IntegerField(label="Length (fts)")
    b_width = forms.IntegerField(label="width of wall (inchs)")
    b_height = forms.IntegerField(label="height (inchs)")
    b_no_of_walls = forms.IntegerField(label="no_of_walls")


class RccSlap(forms.Form):
    s_length = forms.FloatField(label="Length (fts)")
    s_width = forms.IntegerField(label="width of wall (fts)")
    s_height = forms.IntegerField(label="height (inchs)")
    s_no_of_walls = forms.IntegerField(label="no_of_walls")


class Vtoc_req(forms.Form):
    name = forms.CharField(label="Vendor Name", required=True)
    # gmail = forms.EmailField(label="Gmail", max_length=100)
    year_of_experience = forms.IntegerField(
        label="year_of_experience", required=True)
    projects_done = forms.IntegerField(label="projects_done", required=True)
    rating = forms.IntegerField(label="rating", required=True)
    description = forms.CharField(label="Description", required=True)
    image = forms.ImageField(label="Your Image", required=True)
