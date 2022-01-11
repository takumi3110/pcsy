from django.db import models

from user.models import User

status_choice = (
	('作成中', '作成中'),
	('使用中', '使用中'),
	('停止中', '停止中'),
	('廃止予定', '廃止予定'),
	('廃止中', '廃止中'),
	('廃止済', '廃止済')
)


class Site(models.Model):
	name = models.CharField(
		verbose_name='サイト名',
		max_length=50
	)

	category = models.CharField(
		verbose_name='カテゴリー',
		max_length=50,
		null=True,
		blank=True
	)

	description = models.TextField(
		verbose_name='説明',
		null=True,
		blank=True
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=100,
		choices=status_choice
	)

	version = models.PositiveSmallIntegerField(
		verbose_name='バージョン',
		null=True,
		blank=True
	)

	updated_date = models.DateTimeField(
		verbose_name='更新日',
		auto_now=True
	)

	updated_user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		verbose_name='更新者',
		null=True,
		blank=True
	)

	def __str__(self):
		return f'{self.name} ({self.category})'

	class Meta:
		verbose_name = 'サイト'
		verbose_name_plural = 'サイト'


class Tenant(models.Model):
	name = models.CharField(
		verbose_name='テナント名',
		max_length=200
	)

	site = models.ForeignKey(
		Site,
		on_delete=models.CASCADE,
		verbose_name='サイト名',
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=8,
		choices=status_choice,
		default='作成中'
	)

	description = models.TextField(
		verbose_name='説明',
		null=True,
		blank=True
	)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'テナント'
		verbose_name_plural = 'テナント'


class Team(models.Model):

	name = models.CharField(
		verbose_name='チーム名',
		max_length=200
	)

	code = models.CharField(
		verbose_name='チームNo',
		max_length=8,
		null=True,
		blank=True
	)

	description = models.TextField(
		verbose_name='説明',
		null=True,
		blank=True
	)

	tenant = models.ForeignKey(
		Tenant,
		on_delete=models.CASCADE,
		verbose_name='テナント',
		null=True,
		blank=True
	)

	bcp_tenant = models.ForeignKey(
		Tenant,
		on_delete=models.CASCADE,
		verbose_name='BCPテナント',
		null=True,
		blank=True,
		related_name='bcp_tenant'
	)

	start_date = models.DateField(
		verbose_name='利用開始日',
		null=True,
		blank=True
	)

	end_date = models.DateField(
		verbose_name='利用終了日',
		null=True,
		blank=True
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=10,
		choices=status_choice
	)

	proportion = models.BooleanField(
		verbose_name='按分対象',
	)

	updated_user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		verbose_name='更新者',
		null=True,
		blank=True
	)

	updated_date = models.DateTimeField(
		verbose_name='更新日',
		auto_now=True
	)

	def __str__(self):
		if self.code is None:
			return self.name
		else:
			return f'{self.code} {self.name}'

	class Meta:
		verbose_name = 'チーム'
		verbose_name_plural = 'チーム'


class Dept(models.Model):
	dept_choices = (
		('使用中', '使用中'),
		('閉鎖', '閉鎖')
	)

	code = models.CharField(
		verbose_name='部門コード',
		max_length=16,
	)

	name = models.CharField(
		verbose_name='部門名',
		max_length=100
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=20,
		choices=dept_choices,
		null=True,
		blank=True
	)

	aggregate_code = models.PositiveSmallIntegerField(
		verbose_name='集計用コード',
		null=True,
		blank=True
	)

	active = models.BooleanField(
		verbose_name='使用中',
		default=False
	)

	team = models.ForeignKey(
		Team,
		on_delete=models.CASCADE,
		verbose_name='チーム'
	)

	def save(self, *args, **kwargs):
		if self.active:
			self.status = '使用中'
		else:
			self.status = '閉鎖中'
		super(Dept, self).save(*args, **kwargs)

	def __str__(self):
		return f'{self.code} {self.name}'

	class Meta:
		verbose_name = '部門'
		verbose_name_plural = '部門'


class Location(models.Model):
	name = models.CharField(
		verbose_name='拠点名',
		max_length=50
	)

	ridge = models.CharField(
		verbose_name='棟',
		max_length=50
	)

	address = models.CharField(
		verbose_name='住所',
		max_length=255,
		null=True,
		blank=True
	)

	description = models.TextField(
		verbose_name='説明',
		null=True,
		blank=True
	)

	def __str__(self):
		return f'{self.name} ({self.ridge})'

	class Meta:
		verbose_name = '拠点'
		verbose_name_plural = '拠点'
