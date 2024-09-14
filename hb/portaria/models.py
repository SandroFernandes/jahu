from django.db import models
from datetime import datetime
from .utils import is_license_plate_valid
from django.core.exceptions import ValidationError
from django.conf import settings

DOCUMENTO = [
    (1, 'CPF'),
    (2, 'RG'),
    (3, 'RNE'),
    (4, 'CNH'),
    (5, 'CIN'),
    (6, 'Passaporte'),
    (7, 'Sem documento'),
    (9, 'Outro')
]

TIPO_DE_VEICULO = [
    (1, 'Carro'),
    (2, 'Moto'),
    (3, 'Caminhão'),
    (4, 'Van'),
    (5, 'Ônibus'),
    (6, 'Caminhonete'),
    (9, 'Outro')
]

TIPO_DE_VISITANTE = [
    (1, 'Visitante'),
    (2, 'Prestador de serviço'),
    (3, 'Entregador'),
    (4, 'Fornecedor'),
    (5, 'Doméstica'),
    (6, 'Jardineiro'),
    (7, 'Poceiro'),
    (8, 'Corretores de imóveis'),
    (9, 'Provedor de internet'),
    (10, 'Engenheiro'),
    (11, 'Arquiteto'),
    (12, 'Pedreiro'),
    (13, 'Eletricista'),
    (14, 'Pintor'),
    (15, 'Marceneiro'),
    (16, 'Encanador'),
    (17, 'Vidraceiro'),
    (18, 'Serralheiro'),
    (19, 'Bombeiro'),
    (20, 'Policia'),
    (21, 'Ambulância'),
    (22, 'Oficial de Justiça'),
    (23, 'Outro')

]

AGUA = [
    (100, 'Poço Artesiano'),
    (200, 'Poço Semi-artesiano'),
    (300, 'Poço Caipira'),
    (400, 'Carro-pipa'),
    (500, 'ETA'),
    (600, 'Cisterna'),
    (700, 'Publica tratada'),
    (800, 'Outro'),
]

SANEAMENTO = [
    (1000, 'Fossa Séptica'),
    (2000, 'Fossa Negra'),
    (3000, 'Fossa Ecológica'),
    (4000, 'Fossa Seca'),
    (5000, 'Fossa de Bananeira'),
    (6000, 'Fossa de Anéis'),
    (7000, 'Fossa de Máquina de Lavar roupa'),
    (8000, 'Caixa de Gordura'),
    (10000, 'Biodigestor'),
    (11000, 'Outro'),
]


class Atualizado(models.Model):
    """
    Modelo para armazenar alterações de dados
    """

    nome_do_modelo = models.CharField(max_length=100,
                                      verbose_name='Modelo',
                                      help_text='Nome do modelo')

    ultima_atualizacao = models.DateTimeField(auto_now=True,
                                              verbose_name='Última atualização',
                                              help_text='Data da última atualização')

    def __str__(self):
        return self.nome_do_modelo

    def to_dict(self):
        return {
            'nome_do_modelo': self.nome_do_modelo,
            'ultima_atualizacao': self.ultima_atualizacao.strftime(settings.DATETIME_INPUT_FORMATS)
        }

    def to_list(self):
        return [d.to_dict() for d in self.objects.all()]

    def precisa_atualizar(self, data_ultima_atualizacao):
        """
        Verifica se os dados precisam ser atualizados

        Parâmetros
        ----------
        data_ultima_atualizacao : datetime
            Data da última atualização dos dados

        Retorna
        -------
        bool:
            True se os dados precisam ser atualizados, False caso contrário
        """
        return self.objects.filter(ultima_atualizacao__lt=data_ultima_atualizacao).exists()

    class Meta:
        verbose_name = 'Alteração de dados'
        verbose_name_plural = 'Alterações de dados'
        indexes = [
            models.Index(fields=['-ultima_atualizacao']),
        ]


class Cor(models.Model):
    cor = models.CharField(max_length=50,
                           verbose_name='Cor',
                           help_text='Ex: Preto, branco, vermelho, etc.')

    def __str__(self):
        return self.cor

    def to_dict(self):
        return {
            'id': self.pk,
            'cor': self.cor,
        }

    @staticmethod
    def to_list(query):
        return [cor.to_dict() for cor in query]

    @staticmethod
    def field_index():
        return 'cor'

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'
        indexes = [
            models.Index(fields=['cor']),
        ]


class MarcaModelo(models.Model):
    marca_modelo = models.CharField(max_length=50,
                                    verbose_name='Marca/Modelo',
                                    help_text='Ex: Fiat Uno, Volkswagen Gol, etc.')

    tipo = models.IntegerField(choices=TIPO_DE_VEICULO,
                               verbose_name='Tipo',
                               default=1,
                               help_text='Tipo de veículo')

    def __str__(self):
        return self.marca_modelo

    def to_dict(self):
        return {
            'id': self.pk,
            'marca_modelo': self.marca_modelo,
            'tipo': self.tipo,
        }

    @staticmethod
    def to_list():
        return [marca_modelo.to_dict() for marca_modelo in MarcaModelo.objects.all()]

    class Meta:
        verbose_name = 'Marca/Modelo'
        verbose_name_plural = 'Marcas/Modelos'
        indexes = [
            models.Index(fields=['marca_modelo']),
        ]


class Veiculo(models.Model):
    placa = models.CharField(max_length=7,
                             unique=True,
                             verbose_name='Placa',
                             help_text='Apenas números e letras')

    tipo = models.IntegerField(choices=TIPO_DE_VEICULO,
                               verbose_name='Tipo',
                               help_text='Tipo de veículo')

    modelo = models.ForeignKey(MarcaModelo,
                               on_delete=models.DO_NOTHING,
                               verbose_name='Marca/Modelo')

    ano = models.PositiveIntegerField(verbose_name='Ano',
                                      choices=[(i, i) for i in range(datetime.now().year, 1950, -1)],
                                      help_text=f'Ex: {datetime.now().year}.')

    cor = models.ForeignKey(Cor,
                            on_delete=models.DO_NOTHING,
                            verbose_name='Cor')

    ultima_atualizacao = models.DateTimeField(auto_now=True,
                                              editable=False,
                                              verbose_name='Última atualização')

    def __str__(self):
        return self.placa

    def to_dict(self):
        return {
            'id': self.pk,
            'Placa': self.placa,
            'Tipo': self.tipo,
            'Modelo_id': self.modelo_id,
            'Ano': self.ano,
            'Cor_id': self.cor_id,
            'Atualizado': self.ultima_atualizacao.strftime(settings.DATETIME_INPUT_FORMATS)
        }

    @classmethod
    def to_list(cls):
        query = cls.objects.all()
        return [v.to_dict() for v in query], query.count()

    def clean(self):
        self.placa = self.placa.upper()
        if not is_license_plate_valid(self.placa):
            raise ValidationError('Placa inválida')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Veiculo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        indexes = [
            models.Index(fields=['placa', '-ultima_atualizacao']),
        ]


class Morador(models.Model):
    nome = models.CharField(max_length=100,
                            verbose_name='Nome')

    documento = models.CharField(max_length=20,
                                 null=True,
                                 blank=True,
                                 verbose_name='Documento')

    tipo_documento = models.IntegerField(choices=DOCUMENTO,
                                         default=2,
                                         verbose_name='Tipo de documento')

    celular = models.CharField(max_length=11,
                               verbose_name='Celular')

    email = models.EmailField(max_length=100,
                              verbose_name='E-mail')

    veiculos = models.ManyToManyField(Veiculo,
                                      blank=True,
                                      verbose_name='Veículos')

    observacao = models.TextField(null=True,
                                  blank=True,
                                  verbose_name='Observação',
                                  help_text='Informe alguma observação')

    data_inclusao = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Data de inclusão')

    ultima_atualizacao = models.DateTimeField(auto_now=True,
                                              verbose_name='Última atualização')

    def __str__(self):
        return self.nome

    def to_dict(self):
        return {
            'id': self.pk,
            'Nome': self.nome,
            'Documento': self.documento,
            'Tipo de Documento': self.tipo_documento,
            'Celular': self.celular,
            'E-mail': self.email,
            'Veículos': [v.placa for v in self.veiculos.all()],
            'Observação': self.observacao,
            'Data de Inclusão': self.data_inclusao.strftime(settings.DATETIME_INPUT_FORMATS),
            'Última Atualização': self.ultima_atualizacao.strftime(settings.DATETIME_INPUT_FORMATS)
        }

    @classmethod
    def to_list(cls):
        return [m.to_dict() for m in cls.objects.all()]

    def veiculos_list(self):
        return ', '.join([str(v) for v in self.veiculos.all()])

    veiculos_list.short_description = 'Veículos'

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Morador, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Morador'
        verbose_name_plural = 'Moradores'
        ordering = ['nome']


class Lote(models.Model):
    lote = models.CharField(max_length=10,
                            verbose_name='Lote',
                            help_text='Informe o número do lote')

    ultima_atualizacao = models.DateTimeField(auto_now=True,
                                              editable=False,
                                              verbose_name='Última atualização')

    def __str__(self):
        return self.lote

    def to_dict(self):
        return {
            'id': self.pk,
            'Lote': self.lote,
            'Atualizado': self.ultima_atualizacao.strftime(settings.DATETIME_INPUT_FORMATS)
        }

    @classmethod
    def to_list(cls):
        return [l.to_dict() for l in cls.objects.all()]

    class Meta:
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'
        ordering = ['lote']


class Quadra(models.Model):
    quadra = models.CharField(max_length=10,
                              verbose_name='Quadra',
                              help_text='Informe o número da quadra')

    ultima_atualizacao = models.DateTimeField(auto_now=True,
                                              editable=False,
                                              verbose_name='Última atualização')

    def __str__(self):
        return self.quadra

    def to_dict(self):
        return {
            'id': self.pk,
            'Quadra': self.quadra,
            'Atualizado': self.ultima_atualizacao.strftime(settings.DATETIME_INPUT_FORMATS)
        }

    @classmethod
    def to_list(cls):
        return [q.to_dict() for q in cls.objects.all()]


class Residencia(models.Model):
    quadra = models.ForeignKey(Quadra,
                               on_delete=models.DO_NOTHING,
                               verbose_name='Quadra',
                               help_text='Informe a quadra')

    lote = models.ForeignKey(Lote,
                             on_delete=models.DO_NOTHING,
                             verbose_name='Lote',
                             help_text='Informe o lote')

    moradores = models.ManyToManyField(Morador,
                                       verbose_name='Moradores',
                                       help_text='Informe os moradores')

    agua = models.IntegerField(choices=AGUA,
                               verbose_name='Água',
                               help_text='Informe a fonte de água')

    saneamento = models.IntegerField(choices=SANEAMENTO,
                                     verbose_name='Saneamento',
                                     help_text='Informe o tipo de saneamento')

    ultima_atualizacao = models.DateTimeField(auto_now=True,
                                              editable=False,
                                              verbose_name='Última atualização')


class Visitantes(models.Model):
    tipo_visitante = models.IntegerField(choices=TIPO_DE_VISITANTE,
                                         verbose_name='Tipo de visitante',
                                         help_text='Informe o tipo de visitante')
    nome = models.CharField(max_length=100,
                            verbose_name='Nome',
                            help_text='Informe o nome do visitante')

    tipo_de_documento = models.IntegerField(choices=DOCUMENTO,
                                            verbose_name='Tipo de documento',
                                            help_text='Informe o tipo de documento')
    documento = models.CharField(max_length=20,

                                 null=True,
                                 blank=True,
                                 verbose_name='Documento',
                                 help_text='Informe o documento do visitante')

    residencia = models.ForeignKey(Residencia,
                                   on_delete=models.DO_NOTHING,
                                   verbose_name='Residência',
                                   help_text='Informe a residência do visitante')

    morador = models.ForeignKey(Morador,
                                on_delete=models.DO_NOTHING,
                                verbose_name='Morador',
                                help_text='Informe o morador')

    data_entrada = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Data de entrada',
                                        help_text='Informe a data de entrada do visitante')

    data_saida = models.DateTimeField(null=True,
                                      blank=True,
                                      verbose_name='Data de saída',
                                      help_text='Informe a data de saída do visitante')
