from django.db import models

from teamInfo.models import Location


status_choice = (
	('作成中', '作成中'),
	('使用中', '使用中'),
	('停止中', '停止中'),
	('廃止予定', '廃止予定'),
	('廃止中', '廃止中'),
	('廃止済', '廃止済')
)


# Line
class Career(models.Model):
	name = models.CharField(
		verbose_name='キャリア',
		max_length=20
	)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'キャリア'
		verbose_name_plural = 'キャリア'


class Category(models.Model):
	name = models.CharField(
		verbose_name='カテゴリー',
		max_length=50
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=20,
		choices=status_choice
	)

	career = models.ForeignKey(
		Career,
		on_delete=models.CASCADE,
		verbose_name='キャリア'
	)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '回線種別'
		verbose_name_plural = '回線種別'


class ContractNumber(models.Model):
	number = models.CharField(
		verbose_name='契約番号',
		max_length=100
	)

	location = models.ForeignKey(
		Location,
		on_delete=models.CASCADE,
		verbose_name='ロケーション'
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=10,
		choices=status_choice
	)

	start_date = models.DateField(
		verbose_name='利用開始日',
	)

	name = models.CharField(
		verbose_name='契約者名',
		max_length=255
	)

	place = models.CharField(
		verbose_name='回線設置場所',
		max_length=255,
		null=True,
		blank=True
	)

	line_category = models.ForeignKey(
		Category,
		on_delete=models.CASCADE,
		verbose_name='回線種別'
	)

	description = models.TextField(
		verbose_name='説明',
		null=True,
		blank=True
	)

	version = models.PositiveSmallIntegerField(
		verbose_name='バージョン',
		null=True,
		blank=True
	)

	def __str__(self):
		return self.number

	class Meta:
		verbose_name = '契約番号'
		verbose_name_plural = '契約番号'


class ParentNumber(models.Model):
	number = models.CharField(
		verbose_name='親番号',
		max_length=100
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=10,
		choices=status_choice
	)

	line_category = models.ForeignKey(
		Category,
		on_delete=models.CASCADE,
		verbose_name='回線種別'
	)

	description = models.TextField(
		verbose_name='説明',
		null=True,
		blank=True
	)

	def __str__(self):
		return self.number

	class Meta:
		verbose_name = '親番号'
		verbose_name_plural = '親番号'


