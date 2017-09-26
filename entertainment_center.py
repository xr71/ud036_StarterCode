import media
import fresh_tomatoes

# create individual movie instances based on Movie class from media.py
princess_bride = media.Movie('The Princess Bride',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BMGM4M2Q5N2MtNThkZS00NTc1LTk1NTItNWEyZjJjNDRmNDk5XkEyXkFqcGdeQXVyMjA0MDQ0Mjc@._V1_SY1000_CR0,0,676,1000_AL_.jpg',
                        'https://www.youtube.com/watch?v=WNNUcHRiPS8')

hidden_figures = media.Movie('Hidden Figures',
                     'https://images-na.ssl-images-amazon.com/images/M/MV5BMzg2Mzg4YmUtNDdkNy00NWY1LWE3NmEtZWMwNGNlMzE5YzU3XkEyXkFqcGdeQXVyMjA5MTIzMjQ@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
                     'https://www.youtube.com/watch?v=5wfrDhgUMGI')

sw_force_awakens = media.Movie('Star Wars The Force Awakens',
                            'https://images-na.ssl-images-amazon.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_SY1000_CR0,0,677,1000_AL_.jpg',
                            'https://www.youtube.com/watch?v=sGbxmsDFVnE')

cinema_paradiso = media.Movie('Cinema Paradiso',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BM2FhYjEyYmYtMDI1Yy00YTdlLWI2NWQtYmEzNzAxOGY1NjY2XkEyXkFqcGdeQXVyNTA3NTIyNDg@._V1_.jpg',
                        'https://www.youtube.com/watch?v=C2-GX0Tltgw')

good_will_hunting = media.Movie('Good Will Hunting',
                     'https://images-na.ssl-images-amazon.com/images/M/MV5BOTI0MzcxMTYtZDVkMy00NjY1LTgyMTYtZmUxN2M3NmQ2NWJhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,655,1000_AL_.jpg',
                     'https://www.youtube.com/watch?v=PaZVjZEFkRs')

the_pianist = media.Movie('The Pianist',
                            'https://images-na.ssl-images-amazon.com/images/M/MV5BOWRiZDIxZjktMTA1NC00MDQ2LWEzMjUtMTliZmY3NjQ3ODJiXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,724,1000_AL_.jpg',
                            'https://www.youtube.com/watch?v=CIRLLPa-j9o')

# Take movie instances above and put into an array
movies = [princess_bride, hidden_figures, sw_force_awakens, cinema_paradiso, good_will_hunting, the_pianist]

# Use the movies array to generate our webpage
fresh_tomatoes.open_movies_page(movies)