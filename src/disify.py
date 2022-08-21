from requests import get


class Disify:
	def __init__(self):
		self.api = "https://www.disify.com"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def check_email_validation(self, email: str):
		return get(
			f"{self.api}/api/email/{email}",
			headers=self.headers).json()
	
	def check_domain_validation(self, domain: str):
		return get(
			f"{self.api}/api/domain/{domain}",
			headers=self.headers).json()
	
	def view_validation_results(self, session: str):
		return get(
			f"{self.api}/api/view/{session}",
			headers=self.headers).json()
	
	def check_mass_emails_validation(self, emails: str):
		return get(
			f"{self.api}/api/email/{emails}/mass",
			headers=self.headers).json()
	
	def check_mass_domains_validation(self, domains: str):
		return get(
			f"{self.api}/api/domain/{domains}/mass",
			headers=self.headers).json()
	
	def get_black_list_domains(self):
		return get(
			f"{self.api}/blacklist/domains",
			headers=self.headers).text
	
