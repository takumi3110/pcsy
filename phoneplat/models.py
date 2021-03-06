from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


from user.models import User


# Team
status_choice = (
	('作成中', '作成中'),
	('使用中', '使用中'),
	('停止中', '停止中'),
	('廃止予定', '廃止予定'),
	('廃止中', '廃止中')
)


class Site(models.Model):
	name = models.CharField(
		verbose_name='サイト名',
		max_length=200
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
		null=True,
		blank=True
	)

	updated_user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		verbose_name='更新者',
		null=True,
		blank=True
	)

	def save(self, *args, **kwargs):
		self.updated_date = timezone.now()
		super(Site, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

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

	code = models.PositiveSmallIntegerField(
		verbose_name='チームNo',
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

	contact_user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		verbose_name='担当者',
	)

	def __str__(self):
		return f'{self.code} {self.name}'

	class Meta:
		verbose_name = 'チーム'
		verbose_name_plural = 'チーム'


class Dept(models.Model):
	dept_choices = (
		('使用中', '使用中'),
		('閉鎖', '閉鎖')
	)

	name = models.CharField(
		verbose_name='部門名',
		max_length=100
	)

	code = models.PositiveSmallIntegerField(
		verbose_name='部門コード'
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=20,
		choices=dept_choices
	)

	aggregate_code = models.PositiveSmallIntegerField(
		verbose_name='集計用コード'
	)

	active = models.BooleanField(
		verbose_name='使用中',
	)

	team = models.ForeignKey(
		Team,
		on_delete=models.CASCADE,
		verbose_name='チーム'
	)

	def save(self, *args, **kwargs):
		if self.status == '使用中':
			self.active = True
		else:
			self.active = False

	def __str__(self):
		return f'{self.code} {self.name}'

	class Meta:
		verbose_name = '部門'
		verbose_name_plural = '部門'


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


class LineCategory(models.Model):
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


class Location(models.Model):
	name = models.CharField(
		verbose_name='ロケーション',
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
		return self.name

	class Meta:
		verbose_name = 'ロケーション'
		verbose_name_plural = 'ロケーション'


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
		LineCategory,
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

	career = models.ForeignKey(
		Career,
		on_delete=models.CASCADE,
		verbose_name='キャリア'
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=10,
		choices=status_choice
	)

	line_category = models.ForeignKey(
		LineCategory,
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


# Service
class System(models.Model):
	name = models.CharField(
		verbose_name='システム',
		max_length=100
	)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'システム'
		verbose_name_plural = 'システム'


class PhoneNumber(models.Model):
	category_choice = (
		('csim', 'CSIM'),
		('others', '他システム'),
		('fax', '実回線、FAX'),
		('outgoing', '発信専用番号'),
		('surplus', '余剰')
	)

	paying_choice = (
		('自課金', '自課金'),
		('その他', 'その他')
	)

	category = models.CharField(
		verbose_name='カテゴリー',
		max_length=20,
		choices=category_choice
	)

	number = models.CharField(
		verbose_name='電話番号',
		max_length=16,
		# validators=[]

	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=10,
		choices=status_choice
	)

	system = models.ForeignKey(
		System,
		on_delete=models.CASCADE,
		verbose_name='システム'
	)

	opening_date = models.DateField(
		verbose_name='番号開通日',
		null=True,
		blank=True
	)

	end_date = models.DateField(
		verbose_name='番号廃止日',
		null=True,
		blank=True
	)

	start_date = models.DateField(
		verbose_name='利用開始日',
		null=True,
		blank=True
	)

	obsolete_date = models.DateField(
		verbose_name='利用終了日',
		null=True,
		blank=True
	)

	interrupt_date = models.DateField(
		verbose_name='割り込み申込日',
		null=True,
		blank=True
	)

	paying = models.CharField(
		verbose_name='課金先',
		max_length=10,
		choices=paying_choice
	)

	ticket = models.CharField(
		verbose_name='チケット番号',
		max_length=20,
		null=True,
		blank=True
	)

	description = models.TextField(
		verbose_name='説明',
		null=True,
		blank=True
	)

	updated_date = models.DateTimeField(
		verbose_name='更新日',
		null=True,
		blank=True
	)

	updated_user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		verbose_name='更新者',
		null=True,
		blank=True
	)

	def __str__(self):
		return self.number

	class Meta:
		verbose_name = '電話番号'
		verbose_name_plural = '電話番号'


class SurplusNumber(models.Model):
	surplus_choice = (
		('ダミー', 'ダミー'),
		('余剰', '余剰'),
		('予約中', '予約中'),
		('使用中', '使用中'),
		('廃止予定', '廃止予定'),
		('廃止済', '廃止済'),
	)

	number = models.CharField(
		verbose_name='余剰電話番号',
		max_length=20
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=10,
		choices=surplus_choice
	)

	system = models.ForeignKey(
		System,
		on_delete=models.CASCADE,
		verbose_name='システム',
	)

	opening_date = models.DateField(
		verbose_name='番号開通日',
		null=True,
		blank=True
	)

	end_date = models.DateField(
		verbose_name='番号廃止日',
		null=True,
		blank=True
	)

	ticket = models.CharField(
		verbose_name='チケット番号',
		max_length=20,
		null=True,
		blank=True
	)

	description = models.TextField(
		verbose_name='説明',
		null=True,
		blank=True
	)

	updated_date = models.DateTimeField(
		verbose_name='更新日',
		null=True,
		blank=True
	)

	updated_user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		verbose_name='更新者',
		null=True,
		blank=True
	)

	def __str__(self):
		return self.number

	class Meta:
		verbose_name = '電話番号（余剰）'
		verbose_name_plural = '電話番号（余剰）'


class Service(models.Model):
	category_choice = (
		('csim', 'csim'),
		('その他', 'その他')
	)

	number = models.PositiveSmallIntegerField(
		verbose_name='サービスNo'
	)

	name = models.CharField(
		verbose_name='サービス名',
		max_length=255
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=10,
		choices=status_choice
	)

	team = models.ForeignKey(
		Team,
		on_delete=models.CASCADE,
		verbose_name='チーム'
	)

	holiday = models.BooleanField(
		verbose_name='祝日設定',
	)

	always = models.BooleanField(
		verbose_name='24h/365日対応',
	)

	start_date = models.DateField(
		verbose_name='開始日',
		null=True,
		blank=True
	)

	end_date = models.DateField(
		verbose_name='終了日',
		null=True,
		blank=True
	)

	remind = models.CharField(
		verbose_name='リマインド',
		max_length=5,
		choices=(
			('開始', '開始'),
			('終了', '終了')
		),
		null=True,
		blank=True
	)

	channel_count = models.PositiveSmallIntegerField(
		verbose_name='チャンネル数',
		default=0
	)

	description = models.TextField(
		verbose_name='説明',
		null=True,
		blank=True
	)

	mail_address = models.EmailField(
		verbose_name='送信先メールアドレス',
		null=True,
		blank=True
	)

	file = models.FileField(
		null=True,
		blank=True
	)

	version = models.PositiveSmallIntegerField(
		verbose_name='バージョン',
		null=True,
		blank=True
	)

	updated_date = models.DateTimeField(
		verbose_name='更新日',
		null=True,
		blank=True
	)

	updated_user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		verbose_name='更新者',
		null=True,
		blank=True
	)

	contract_number = models.ForeignKey(
		ContractNumber,
		on_delete=models.CASCADE,
		verbose_name='契約番号',
		null=True,
		blank=True
	)

	line_category = models.ForeignKey(
		LineCategory,
		on_delete=models.CASCADE,
		verbose_name='回線種別',
		null=True,
		blank=True
	)

	parent_number = models.ForeignKey(
		ParentNumber,
		on_delete=models.CASCADE,
		verbose_name='親番号',
		null=True,
		blank=True
	)

	def __str__(self):
		return f'{self.number} {self.name}'

	class Meta:
		verbose_name = 'サービス'
		verbose_name_plural = 'サービス'


class AccessLine(models.Model):
	location = models.ForeignKey(
		Location,
		on_delete=models.CASCADE,
		verbose_name='ロケーション'
	)

	system = models.ForeignKey(
		System,
		on_delete=models.CASCADE,
		verbose_name='システム'
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=10,
		choices=status_choice
	)

	career = models.ForeignKey(
		Career,
		on_delete=models.CASCADE,
		verbose_name='キャリア'
	)

	line_category = models.ForeignKey(
		LineCategory,
		on_delete=models.CASCADE,
		verbose_name='回線種別'
	)

	parent_number = models.ForeignKey(
		ParentNumber,
		on_delete=models.CASCADE,
		verbose_name='親番号'
	)

	opening_date = models.DateField(
		verbose_name='開通日',
		null=True,
		blank=True
	)

	contract_number = models.ForeignKey(
		ContractNumber,
		on_delete=models.CASCADE,
		verbose_name='契約番号'
	)

	proportion = models.BooleanField(
		verbose_name='按分集計対象'
	)

	surplus_count = models.PositiveSmallIntegerField(
		verbose_name='余剰数',
		default=0
	)

	allowance_count = models.PositiveSmallIntegerField(
		verbose_name='余裕数',
		default=0
	)

	threshold_value = models.PositiveSmallIntegerField(
		verbose_name='しきい値',
		default=0
	)

	updated_date = models.DateField(
		verbose_name='更新日',
		null=True,
		blank=True
	)

	updated_user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		verbose_name='更新者'
	)

	def __str__(self):
		return f'{self.parent_number.number} {self.location.name}'

	class Meta:
		verbose_name = 'アクセス回線'
		verbose_name_plural = 'アクセス回線'


class Trank(models.Model):
	name = models.CharField(
		verbose_name='トランク名',
		max_length=50
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

	description = models.TextField(
		verbose_name='説明',
		null=True,
		blank=True
	)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'トランク'
		verbose_name_plural = 'トランク'


class Scenario(models.Model):
	number = models.CharField(
		verbose_name='シナリオNo',
		max_length=50
	)

	name = models.CharField(
		verbose_name='シナリオ名',
		max_length=100
	)

	service = models.ForeignKey(
		Service,
		on_delete=models.CASCADE,
		verbose_name='サービス名'
	)

	team = models.ForeignKey(
		Team,
		on_delete=models.CASCADE,
		verbose_name='チーム名'
	)

	description = models.TextField(
		verbose_name='説明',
		null=True,
		blank=True
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=10,
		choices=status_choice
	)

	updated_user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		verbose_name='更新者'
	)

	updated_date = models.DateTimeField(
		verbose_name='更新日',
		null=True,
		blank=True
	)

	def __str__(self):
		return f'{self.number}{self.name}'

	class Meta:
		verbose_name = 'シナリオ'
		verbose_name_plural = 'シナリオ'


class TrankInfo(models.Model):
	trank_primary = models.ForeignKey(
		Trank,
		on_delete=models.CASCADE,
		verbose_name='トランク1',
		related_name='trank_primary'
	)

	trank_secondary = models.ForeignKey(
		Trank,
		on_delete=models.CASCADE,
		verbose_name='トランク2',
		null=True,
		blank=True,
		related_name='trank_secondary'
	)

	prefix_primary = models.PositiveSmallIntegerField(
		verbose_name='プレフィックス1'
	)

	prefix_secondary = models.PositiveSmallIntegerField(
		verbose_name='プレフィックス2',
		null=True,
		blank=True
	)

	access_line = models.ForeignKey(
		AccessLine,
		on_delete=models.CASCADE,
		verbose_name='アクセス回線'
	)

	def __str__(self):
		return self.trank_primary

	class Meta:
		verbose_name = 'トランク情報'
		verbose_name_plural = 'トランク情報'


# Paying
class PayingService(models.Model):
	name = models.CharField(
		verbose_name='着信課金サービス名',
		max_length=50
	)

	career = models.ForeignKey(
		Career,
		on_delete=models.CASCADE,
		verbose_name='キャリア'
	)

	def __str__(self):
		return f'{self.name} {self.career.name}'

	class Meta:
		verbose_name = '着信課金サービス'
		verbose_name_plural = '着信課金サービス'


class IncomingNumber(models.Model):
	holder_choice = (
		('PI', 'PI'),
		('CL', 'CL')
	)

	number = models.CharField(
		verbose_name='着信課金番号',
		max_length=16
	)

	paying_service = models.ForeignKey(
		PayingService,
		on_delete=models.CASCADE,
		verbose_name='着信課金サービス'
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=10,
		choices=status_choice
	)

	holder = models.CharField(
		verbose_name='名義',
		max_length=4,
		choices=holder_choice
	)

	channel_count = models.PositiveSmallIntegerField(
		verbose_name='FD-CH数'
	)

	start_date = models.DateField(
		verbose_name='利用開始日',
		null=True,
		blank=True
	)

	country = models.CharField(
		verbose_name='提供対地',
		max_length=50
	)

	description = models.TextField(
		verbose_name='説明',
		null=True,
		blank=True
	)

	updated_user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		verbose_name='更新者'
	)

	updated_date = models.DateTimeField(
		verbose_name='更新日',
		null=True,
		blank=True
	)

	def __str__(self):
		return self.number

	class Meta:
		verbose_name = '着信課金番号'
		verbose_name_plural = '着信課金番号'


class PayingCode(models.Model):
	paying_choice = (
		('余剰', '余剰'),
		('使用中', '使用中'),
		('TEMS削除待ち', 'TEMS削除待ち'),
		('廃止済み', '廃止済み')
	)
	code = models.PositiveSmallIntegerField(
		verbose_name='課金コード',
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=10,
		choices=paying_choice
	)

	service = models.ForeignKey(
		Service,
		on_delete=models.CASCADE,
		verbose_name='サービス名'
	)

	dept = models.ForeignKey(
		Dept,
		on_delete=models.CASCADE,
		verbose_name='部門コード'
	)

	target = models.CharField(
		verbose_name='対象DID',
		max_length=16
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

	tems = models.BooleanField(
		verbose_name='TEMS連携',
	)

	tems_date = models.DateField(
		verbose_name='TEMS反映日'
	)

	file = models.FileField(
		null=True,
		blank=True
	)

	ticket_number = models.PositiveIntegerField(
		verbose_name='チケット番号',
		null=True,
		blank=True
	)

	def __str__(self):
		return self.code

	class Meta:
		verbose_name = '課金コード'
		verbose_name_plural = '課金コード'


class Notification(models.Model):
	number = models.CharField(
		verbose_name='通知番号',
		max_length=16
	)

	incoming_number = models.ForeignKey(
		IncomingNumber,
		on_delete=models.CASCADE,
		verbose_name='着信課金番号'
	)

	phone_number = models.ForeignKey(
		PhoneNumber,
		on_delete=models.CASCADE,
		verbose_name='発信専用番号',
		null=True,
		blank=True
	)

	description = models.TextField(
		verbose_name='説明',
		null=True,
		blank=True
	)

	paying_code = models.ForeignKey(
		PayingCode,
		on_delete=models.CASCADE,
		verbose_name='課金コード'
	)

	def __str__(self):
		return self.number

	class Meta:
		verbose_name = '通知番号'
		verbose_name_plural = '通知番号'
