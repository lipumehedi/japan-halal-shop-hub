# Japan Halal Shop Hub (Django)

A beginner-friendly MVP for discovering halal groceries, restaurants, butchers and online shops in Japan. It includes searchable listings, prefecture/category/status filters, shop detail pages, customer reviews with moderation, shop submission with admin approval, and a Django admin panel.

> **Important:** This is a demo starter project, not a halal certification authority. Demo entries are fictional. Do not publish them as real businesses. Confirm all halal claims and obtain permission for business information and images.

## Features
- Search by shop name, city, address or description
- Filter by prefecture, category and halal-status label
- Shop detail pages with address, hours, phone and website
- Public shop submissions held for admin approval
- Customer reviews held for admin approval
- Django admin to manage listings and reviews
- Responsive layout for desktop and mobile
- SQLite for local development

## 1. Requirements
- Python 3.11+ recommended
- VS Code
- Internet connection for the initial Django install

## 2. Open the project in VS Code
Extract the ZIP, open the `japan_halal_shop_hub` folder in VS Code, then open **Terminal → New Terminal**.

### Windows PowerShell
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver
```
Open `http://127.0.0.1:8000/`.

If PowerShell blocks activation, run this only for the current terminal session:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```
Alternatively, use Command Prompt:
```bat
.venv\Scripts\activate.bat
```

## 3. Admin panel
Open `http://127.0.0.1:8000/admin/` and sign in with the superuser you created.
- Approve or reject submitted shops using `Is approved`.
- Review submitted customer reviews and set `Is approved`.
- Change a shop's slug if you need a custom URL.
- Delete the fictional demo entries before real launch.

## 4. Project structure
```text
japan_halal_shop_hub/
├── manage.py
├── requirements.txt
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── shops/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── management/commands/seed_demo.py
├── templates/
│   ├── base.html
│   └── shops/
└── static/css/site.css
```

## 5. How the app works
1. A visitor searches or filters approved listings.
2. A visitor opens a shop page and checks details.
3. A visitor can submit a review; it stays hidden until approved.
4. A shop owner/customer can submit a listing; it stays hidden until approved.
5. An admin verifies the information and publishes it.

## 6. Suggested roadmap to make this a real business
1. **Accuracy and trust:** Create a clear evidence policy for halal status, certification issuer/expiry date, last-checked date and who checked it. Never mark a shop “certified” without documentary verification.
2. **Japanese + English + Bengali:** Add Django translation support and language switcher.
3. **Maps:** Add map links or a maps API; protect API keys and respect usage terms.
4. **Shop owner accounts:** Add authentication and let owners claim listings.
5. **Better moderation:** Add spam protection, rate limiting, reporting and review removal workflow.
6. **Photos:** Add Django image uploads, validate file type/size, and store images in suitable object storage for production.
7. **SEO:** Add canonical URLs, Open Graph tags, sitemap, structured data only for verified facts.
8. **Production database:** Use PostgreSQL, environment variables and secure settings.
9. **Deployment:** Deploy to a service such as Render; configure `DEBUG=False`, a strong secret key, allowed hosts, HTTPS, static files and backups.
10. **Business model:** Optional paid verified profiles, promoted listings clearly labelled as ads, owner analytics and multilingual profile support.

## 7. Before deploying publicly
- Replace the development `SECRET_KEY` with an environment variable.
- Set `DEBUG=False` and configure `ALLOWED_HOSTS`.
- Use PostgreSQL for production and set up backups.
- Configure HTTPS, secure cookies, static/media storage and error monitoring.
- Add privacy policy, terms of use, contact details, takedown/reporting process and consent for reviews.
- Do not collect unnecessary personal information.
- Test shop submission, review moderation, search and mobile layout.
- Replace all demo entries with real listings that you have permission to publish.

## 8. Useful commands
```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver
```
