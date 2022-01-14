from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

from user.models import User
from teamInfo.models import *
from line.models import *


status_choice = (
	('作成中', '作成中'),
	('使用中', '使用中'),
	('停止中', '停止中'),
	('廃止予定', '廃止予定'),
	('廃止中', '廃止中'),
	('廃止済', '廃止済'),
	('余剰', '余剰')
)


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


class Service(models.Model):
	category_choice = (
		('CSIM', 'CSIM'),
		('その他', 'その他')
	)

	category = models.CharField(
		verbose_name='カテゴリー',
		max_length=8,
		choices=category_choice,
	)

	number = models.CharField(
		verbose_name='サービスNo',
		max_length=8,
		blank=True
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
		default=False
	)

	always = models.BooleanField(
		verbose_name='24h/365日対応',
		default=False
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
		default=0,
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
		auto_now=True
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
		Category,
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
		verbose_name='サービス名',
		null=True,
		blank=True
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
		verbose_name='更新者',
		null=True,
		blank=True
	)

	updated_date = models.DateTimeField(
		verbose_name='更新日',
		auto_now=True
	)

	def __str__(self):
		return f'{self.number} {self.name}'

	class Meta:
		verbose_name = 'シナリオ'
		verbose_name_plural = 'シナリオ'


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

	scenario = models.ForeignKey(
		Scenario,
		on_delete=models.CASCADE,
		verbose_name='シナリオ',
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
		return self.number

	class Meta:
		verbose_name = '電話番号（余剰）'
		verbose_name_plural = '電話番号（余剰）'


class AccessLine(models.Model):
	location = models.ForeignKey(
		Location,
		on_delete=models.CASCADE,
		verbose_name='ロケーション'
	)

	system = models.ForeignKey(
		System,
		on_delete=models.CASCADE,
		verbose_name='システム',
		null=True,
		blank=True
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=10,
		choices=status_choice
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
		verbose_name='契約番号',
		null=True,
		blank=True
	)

	proportion = models.BooleanField(
		verbose_name='按分集計対象',
		default=False
	)

	surplus_count = models.PositiveSmallIntegerField(
		verbose_name='余剰数',
		default=0
	)

	allowance_count = models.SmallIntegerField(
		verbose_name='余裕数',
		default=0
	)

	threshold_value = models.PositiveSmallIntegerField(
		verbose_name='しきい値',
		default=0
	)

	updated_date = models.DateField(
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
		return f'{self.parent_number.number} {self.location.name} ({self.location.ridge})'

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

	abbreviation = models.CharField(
		verbose_name='略称',
		max_length=12,
		blank=True
	)

	career = models.ForeignKey(
		Career,
		on_delete=models.CASCADE,
		verbose_name='キャリア'
	)

	def __str__(self):
		if self.abbreviation == '':
			return self.name
		else:
			return f'{self.abbreviation}({self.name})'

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
		max_length=32
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
		choices=holder_choice,
		null=True,
		blank=True
	)

	channel_count = models.PositiveSmallIntegerField(
		verbose_name='FD-CH数'
	)

	target_did = models.CharField(
		verbose_name='対象DID',
		max_length=24,
		blank=True
	)

	service = models.ForeignKey(
		Service,
		on_delete=models.CASCADE,
		verbose_name='サービス',
		null=True,
		blank=True
	)

	start_date = models.DateField(
		verbose_name='利用開始日',
		null=True,
		blank=True
	)

	country = models.CharField(
		verbose_name='提供対地',
		max_length=50,
		null=True,
		blank=True
	)

	description = models.TextField(
		verbose_name='説明',
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

	updated_date = models.DateTimeField(
		verbose_name='更新日',
		auto_now=True
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
		('廃止済', '廃止済')
	)
	code = models.CharField(
		verbose_name='課金コード',
		max_length=8
	)

	status = models.CharField(
		verbose_name='ステータス',
		max_length=10,
		choices=paying_choice
	)

	service = models.ForeignKey(
		Service,
		on_delete=models.CASCADE,
		verbose_name='サービス名',
		null=True,
		blank=True
	)

	dept = models.ForeignKey(
		Dept,
		on_delete=models.CASCADE,
		verbose_name='部門コード'
	)

	target = models.CharField(
		verbose_name='対象DID',
		max_length=16,
		null=True,
		blank=True
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
		verbose_name='TEMS反映日',
		null=True,
		blank=True
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
