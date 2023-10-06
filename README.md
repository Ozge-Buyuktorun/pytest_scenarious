# PYTEST TEST
## Some Examples
base URL : https://practicetestautomation.com/practice/
- Negative Scenarious
- Positive Scenarios
  
### Test case 1: Positive Login test
  Open page
  Type username student into Username field
  Type password Password123 into Password field
  Puch Submit button
  Verify new page URL contains practicetestautomation.com/logged-in-successfully/
  Verify new page contains expected text ('Congratulations' or 'successfully logged in')
  Verify button Log out is displayed on the new page

### Test case 2: Negative username test
  Open page
  Type username incorrectUser into Username field
  Type password Password123 into Password field
  Puch Submit button
  Verify error message is displayed
  Verify error message text is Your username is invalid!
### Test case 3: Negative password test
  Open page
  Type username student into Username field
  Type password incorrectPassword into Password field
  Puch Submit button
  Verify error message is displayed
  Verify error message text is Your password is invalid!
### Result ScreenShot
- ![WhatsApp Görsel 2023-10-04 saat 15 46 49_3275f36b](https://github.com/Ozge-Buyuktorun/Pytest-Senaryo/assets/74399824/835f6145-ccc1-492a-be9f-6dabedeab451)
~~~~~~
![paralel_tests](https://github.com/Ozge-Buyuktorun/Pytest-Senaryo/assets/74399824/f8363a8c-9a3f-4d2a-9cdd-42bf99e49891)

## Some html report example:
![report html](https://github.com/Ozge-Buyuktorun/Pytest-Senaryo/assets/74399824/40165944-87c3-475a-a2f2-517dae49a326)


