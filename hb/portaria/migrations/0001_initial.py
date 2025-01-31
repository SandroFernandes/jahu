# Generated by Django 5.1.1 on 2024-09-12 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.CharField(help_text='Informe o número do lote', max_length=10, verbose_name='Lote')),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
            ],
            options={
                'verbose_name': 'Lote',
                'verbose_name_plural': 'Lotes',
                'ordering': ['lote'],
            },
        ),
        migrations.CreateModel(
            name='Morador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('documento', models.CharField(blank=True, max_length=20, null=True, verbose_name='Documento')),
                ('tipo_documento', models.IntegerField(choices=[(1, 'CPF'), (2, 'RG'), (3, 'RNE'), (4, 'CNH'), (5, 'CIN'), (6, 'Passaporte'), (7, 'Sem documento'), (9, 'Outro')], default=2, verbose_name='Tipo de documento')),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('observacao', models.TextField(blank=True, help_text='Informe alguma observação', null=True, verbose_name='Observação')),
                ('data_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Data de inclusão')),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
            ],
            options={
                'verbose_name': 'Morador',
                'verbose_name_plural': 'Moradores',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Quadra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quadra', models.CharField(help_text='Informe o número da quadra', max_length=10, verbose_name='Quadra')),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
            ],
        ),
        migrations.CreateModel(
            name='Atualizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_modelo', models.CharField(help_text='Nome do modelo', max_length=100, verbose_name='Modelo')),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True, help_text='Data da última atualização', verbose_name='Última atualização')),
            ],
            options={
                'verbose_name': 'Alteração de dados',
                'verbose_name_plural': 'Alterações de dados',
                'indexes': [models.Index(fields=['-ultima_atualizacao'], name='portaria_at_ultima__050fd8_idx')],
            },
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(help_text='Ex: Preto, branco, vermelho, etc.', max_length=50, verbose_name='Cor')),
            ],
            options={
                'verbose_name': 'Cor',
                'verbose_name_plural': 'Cores',
                'indexes': [models.Index(fields=['cor'], name='portaria_co_cor_84a9b1_idx')],
            },
        ),
        migrations.CreateModel(
            name='MarcaModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_modelo', models.CharField(help_text='Ex: Fiat Uno, Volkswagen Gol, etc.', max_length=50, verbose_name='Marca/Modelo')),
                ('tipo', models.IntegerField(choices=[(1, 'Carro'), (2, 'Moto'), (3, 'Caminhão'), (4, 'Van'), (5, 'Ônibus'), (6, 'Caminhonete'), (9, 'Outro')], default=1, help_text='Tipo de veículo', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Marca/Modelo',
                'verbose_name_plural': 'Marcas/Modelos',
                'indexes': [models.Index(fields=['marca_modelo'], name='portaria_ma_marca_m_770dcd_idx')],
            },
        ),
        migrations.CreateModel(
            name='Residencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agua', models.IntegerField(choices=[(100, 'Poço Artesiano'), (200, 'Poço Semi-artesiano'), (300, 'Poço Caipira'), (400, 'Carro-pipa'), (500, 'ETA'), (600, 'Cisterna'), (700, 'Publica tratada'), (800, 'Outro')], help_text='Informe a fonte de água', verbose_name='Água')),
                ('saneamento', models.IntegerField(choices=[(1000, 'Fossa Séptica'), (2000, 'Fossa Negra'), (3000, 'Fossa Ecológica'), (4000, 'Fossa Seca'), (5000, 'Fossa de Bananeira'), (6000, 'Fossa de Anéis'), (7000, 'Fossa de Máquina de Lavar roupa'), (8000, 'Caixa de Gordura'), (10000, 'Biodigestor'), (11000, 'Outro')], help_text='Informe o tipo de saneamento', verbose_name='Saneamento')),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('lote', models.ForeignKey(help_text='Informe o lote', on_delete=django.db.models.deletion.DO_NOTHING, to='portaria.lote', verbose_name='Lote')),
                ('moradores', models.ManyToManyField(help_text='Informe os moradores', to='portaria.morador', verbose_name='Moradores')),
                ('quadra', models.ForeignKey(help_text='Informe a quadra', on_delete=django.db.models.deletion.DO_NOTHING, to='portaria.quadra', verbose_name='Quadra')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(help_text='Apenas números e letras', max_length=7, unique=True, verbose_name='Placa')),
                ('tipo', models.IntegerField(choices=[(1, 'Carro'), (2, 'Moto'), (3, 'Caminhão'), (4, 'Van'), (5, 'Ônibus'), (6, 'Caminhonete'), (9, 'Outro')], help_text='Tipo de veículo', verbose_name='Tipo')),
                ('ano', models.PositiveIntegerField(choices=[(2024, 2024), (2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951)], help_text='Ex: 2024.', verbose_name='Ano')),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='portaria.cor', verbose_name='Cor')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='portaria.marcamodelo', verbose_name='Marca/Modelo')),
            ],
            options={
                'verbose_name': 'Veículo',
                'verbose_name_plural': 'Veículos',
            },
        ),
        migrations.AddField(
            model_name='morador',
            name='veiculos',
            field=models.ManyToManyField(blank=True, to='portaria.veiculo', verbose_name='Veículos'),
        ),
        migrations.CreateModel(
            name='Visitantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_visitante', models.IntegerField(choices=[(1, 'Visitante'), (2, 'Prestador de serviço'), (3, 'Entregador'), (4, 'Fornecedor'), (5, 'Doméstica'), (6, 'Jardineiro'), (7, 'Poceiro'), (8, 'Corretores de imóveis'), (9, 'Provedor de internet'), (10, 'Engenheiro'), (11, 'Arquiteto'), (12, 'Pedreiro'), (13, 'Eletricista'), (14, 'Pintor'), (15, 'Marceneiro'), (16, 'Encanador'), (17, 'Vidraceiro'), (18, 'Serralheiro'), (19, 'Bombeiro'), (20, 'Policia'), (21, 'Ambulância'), (22, 'Oficial de Justiça'), (23, 'Outro')], help_text='Informe o tipo de visitante', verbose_name='Tipo de visitante')),
                ('nome', models.CharField(help_text='Informe o nome do visitante', max_length=100, verbose_name='Nome')),
                ('tipo_de_documento', models.IntegerField(choices=[(1, 'CPF'), (2, 'RG'), (3, 'RNE'), (4, 'CNH'), (5, 'CIN'), (6, 'Passaporte'), (7, 'Sem documento'), (9, 'Outro')], help_text='Informe o tipo de documento', verbose_name='Tipo de documento')),
                ('documento', models.CharField(blank=True, help_text='Informe o documento do visitante', max_length=20, null=True, verbose_name='Documento')),
                ('data_entrada', models.DateTimeField(auto_now_add=True, help_text='Informe a data de entrada do visitante', verbose_name='Data de entrada')),
                ('data_saida', models.DateTimeField(blank=True, help_text='Informe a data de saída do visitante', null=True, verbose_name='Data de saída')),
                ('morador', models.ForeignKey(help_text='Informe o morador', on_delete=django.db.models.deletion.DO_NOTHING, to='portaria.morador', verbose_name='Morador')),
                ('residencia', models.ForeignKey(help_text='Informe a residência do visitante', on_delete=django.db.models.deletion.DO_NOTHING, to='portaria.residencia', verbose_name='Residência')),
            ],
        ),
        migrations.AddIndex(
            model_name='veiculo',
            index=models.Index(fields=['placa', '-ultima_atualizacao'], name='portaria_ve_placa_aeebeb_idx'),
        ),
    ]
