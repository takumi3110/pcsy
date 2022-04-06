class onClickVisible {
	constructor() {
		this.filterMenu = document.querySelector('.filter__open');
		this.resultMenu = document.querySelector('.result__open');
		this.openFilter = document.querySelector('.open-filter');
		this.openResult = document.querySelector('.open-result');
		this.closeFilter = document.querySelector('.close-filter');
		this.closeResult = document.querySelector('.close-result');
		this._init();
	}

	_init() {
		const filterMenu = this.filterMenu;
		const resultMenu = this.resultMenu;
		const openFilter = this.openFilter;
		const openResult = this.openResult;
		const closeFilter = this.closeFilter;
		const closeResult = this.closeResult;
		const defaultMenu = [openFilter, openResult]
		this._noElement(defaultMenu);
		this._clickOpen(openFilter, filterMenu);
		this._clickOpen(openResult, resultMenu);
		this._clickClose(closeFilter, openFilter, filterMenu);
		this._clickClose(closeResult, openResult, resultMenu);
	}

	_clickOpen(el, menu) {
		el.addEventListener('click', () => {
			menu.style.display = '';
			el.style.display = 'none';
		});
	}

	_clickClose(el, openEl, closeEl) {
		el.addEventListener('click', () => {
			openEl.style.display = '';
			closeEl.style.display = 'none';
		});
	}

	_noElement(els) {
		els.forEach((el) => {
			el.style.display = 'none';
		});
	}
}
