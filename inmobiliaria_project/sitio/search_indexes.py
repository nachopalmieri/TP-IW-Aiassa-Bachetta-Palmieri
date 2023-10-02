from haystack import indexes
from .models import Publicacion

class PublicacionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    titulo = indexes.CharField(model_attr='titulo')
    descripcion = indexes.CharField(model_attr='descripcion')
    tipo_operacion = indexes.CharField(model_attr='tipo_operacion')
    tipo_propiedad = indexes.CharField(model_attr='tipo_propiedad')
    id = indexes.IntegerField(model_attr='id')
    ciudad = indexes.CharField(model_attr='ciudad')
    provincia = indexes.CharField(model_attr='provincia')
    autor = indexes.CharField(model_attr='autor')
    fecha_creacion = indexes.DateTimeField(model_attr='fecha_creacion')
    precio = indexes.DecimalField(model_attr='precio')
    expensas = indexes.DecimalField(model_attr='expensas')
    imagen_principal = indexes.CharField(model_attr='imagen_principal')
    image2 = indexes.CharField(model_attr='image2')
    image3 = indexes.CharField(model_attr='image3')
    image4 = indexes.CharField(model_attr='image4')

    def get_model(self):
        return Publicacion

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(estado='publicada')