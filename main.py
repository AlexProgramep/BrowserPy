import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction, QLineEdit, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl('http://google.com'))
		self.setCentralWidget(self.browser)
		self.setWindowTitle("PyQt5 Браузер")
		self.setGeometry(350, 100, 700, 500)
		self.show()

		navbar = QToolBar()
		self.addToolBar(navbar)

		back_btn = QAction('◀ ', self)
		back_btn.triggered.connect(self.browser.back)
		navbar.addAction(back_btn)

		forward_btn = QAction('▶', self)
		forward_btn.triggered.connect(self.browser.forward)
		navbar.addAction(forward_btn)

		reload_btn = QAction('🔁', self)
		reload_btn.triggered.connect(self.browser.reload)
		navbar.addAction(reload_btn)

		home_btn = QAction('🏚', self)
		home_btn.triggered.connect(self.navigate_home)
		navbar.addAction(home_btn)

		home_btn = QAction('❌', self)
		home_btn.triggered.connect(self.clear)
		navbar.addAction(home_btn)

		self.url_bar = QLineEdit()
		self.url_bar.returnPressed.connect(self.navigate_to_url)
		navbar.addWidget(self.url_bar)

		self.browser.urlChanged.connect(self.update_url)
		self.browser.loadFinished.connect(self.update_title)

	def navigate_home(self):
		self.browser.setUrl(QUrl('http://google.com'))

	def clear(self):
		self.browser.setUrl(QUrl(""))

	def navigate_to_url(self):
		q = QUrl(self.url_bar.text())
		if q.scheme() == "":
			q.setScheme("https")

		self.browser.setUrl(q)

	def update_url(self, q):
		self.url_bar.setText(q.toString())

	def update_title(self):
		title = self.browser.page().title()
		self.setWindowTitle(f"{title}  |  PyQt5 Браузер")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	app.exec()
