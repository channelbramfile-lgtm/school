from django import template

register = template.Library()

@register.filter
def selisih_hari(tgl_akhir, tgl_awal):
    if tgl_akhir and tgl_awal:
        return (tgl_akhir - tgl_awal).days
    return 0
