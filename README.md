# Coverage Compass

Coverage Compass is a web application developed during BlasterHacks, a hackathon sponsored by Colorado School of Mines. This application empowers users to swiftly and efficiently search their local area to identify medical providers that accept their insurance, thereby avoiding the inconvenience of insurance denial, especially in urgent situations.

Designed with user experience in mind, Coverage Compass ensures that in times of need, individuals can secure the healthcare services they require without the added stress of navigating insurance complexities.

## Features

- Clean User UI
- Map of Insurance Covered Healthcare Providers


## Usage

1. Select Your Insurance Provider
2. Select Your Insurance Plan
3. Enter Your Zipcode
4. Interact with the Map to find Medical Services 


## Built With

* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - The markup language used for structuring the website.
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - The style sheet language used for describing the look and formatting of the website. Styles are defined in `static/css/stylesPage1.css` and `static/css/stylesPage2.css`.
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - Used for dynamic content on the website. The script `static/js/script.js` is included in the project.
* [Python](https://www.python.org/) - The main programming language used to run the backend and map functionality. Key Python files include `server.py`, `get_map.py`, and several insurance provider scripts like `anthem.py`, `bcbs.py`, `cigna.py`, etc.
* [Flask](http://flask.pocoo.org/) - A micro web framework written in Python for serving the web pages and handling backend logic. Flask is assumed to be part of `requirements.txt`.
* [Geopy](https://geopy.readthedocs.io) - A Python library used for geocoding addresses into latitude and longitude and vice versa, likely essential for mapping functionalities in scripts like `get_map.py`.
* [Folium](https://python-visualization.github.io/folium/) - A Python library used to create interactive leaflet maps. Its use suggests that the project generates dynamic maps, possibly rendered in `coveragemap.html` or served via Flask routes.

Make sure to check `requirements.txt` for a full list of Python libraries used in this project, which include Flask, Pandas, Geopy, and Folium. 

The project uses various data files stored in the `data files` directory, including `ProviderLocPhone.csv` for provider information and `zipToLoc.txt` possibly for mapping ZIP codes to locations.

## Static Content and Templates

- Static content such as images (`logo.png`, `background2.png`), CSS, and JavaScript are stored under the `static` directory.
- HTML templates used by Flask are located in the `templates` directory, including `index.html`, `error.html`, and `map.html` for different views of the application.

## Authors

* **Sam Abderholde --**  [SamAbderholden](https://github.com/yourname)
* **Brenden Maroney --**  [brendanMoro](https://github.com/yourname)
* **Zach Samuels --**  [zachsamuels](https://github.com/yourname)
* **Jack "Siggy" Sigler --**  [sigggy](https://github.com/yourname)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

