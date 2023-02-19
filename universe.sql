--
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-2.pgdg20.04+1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-2.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE universe;
--
-- Name: universe; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE universe WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE universe OWNER TO freecodecamp;

\connect universe

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: galaxy; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.galaxy (
    galaxy_id integer NOT NULL,
    distance_to_earth numeric(9,2),
    age_in_millions_of_years integer,
    galaxy_type text,
    name character varying(50) NOT NULL
);


ALTER TABLE public.galaxy OWNER TO freecodecamp;

--
-- Name: moon; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.moon (
    is_spherical boolean,
    distance_from_planet integer,
    planet_id integer,
    moon_id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.moon OWNER TO freecodecamp;

--
-- Name: planet; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.planet (
    average_temp integer,
    has_life boolean,
    star_id integer,
    planet_id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.planet OWNER TO freecodecamp;

--
-- Name: spaceship; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.spaceship (
    planet_visited_id integer,
    year_launched integer NOT NULL,
    spaceship_id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.spaceship OWNER TO freecodecamp;

--
-- Name: star; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.star (
    galaxy_id integer,
    color character varying(20),
    mass_in_tons numeric(20,4),
    star_id integer NOT NULL,
    name character varying(5) NOT NULL
);


ALTER TABLE public.star OWNER TO freecodecamp;

--
-- Data for Name: galaxy; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.galaxy VALUES (1, 25.00, 13, 'spiral', 'milky way');
INSERT INTO public.galaxy VALUES (2, 200.00, 13, 'dwarf', 'peekaboo');
INSERT INTO public.galaxy VALUES (3, 30.00, 13, 'spiral', 'sombrero');
INSERT INTO public.galaxy VALUES (4, 500.00, 200, 'lenticular', 'cartwhell');
INSERT INTO public.galaxy VALUES (5, 0.12, 30, 'peculiar', 'hoag');
INSERT INTO public.galaxy VALUES (6, 10.00, 25, 'dumas', 'black eye');


--
-- Data for Name: moon; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.moon VALUES (true, 384, 1, 1, 'luna');
INSERT INTO public.moon VALUES (false, 0, 1, 2, 'thungu');
INSERT INTO public.moon VALUES (true, 120, 2, 3, 'trang');
INSERT INTO public.moon VALUES (false, 13, 2, 4, 'bay');
INSERT INTO public.moon VALUES (true, 11, 3, 5, 'namkhanh');
INSERT INTO public.moon VALUES (false, 12, 3, 6, 'nguyetminh');
INSERT INTO public.moon VALUES (true, 8, 4, 7, 'duong');
INSERT INTO public.moon VALUES (false, 12, 4, 8, 'kien');
INSERT INTO public.moon VALUES (true, 17, 5, 9, 'benny');
INSERT INTO public.moon VALUES (false, 19, 5, 10, 'thang');
INSERT INTO public.moon VALUES (true, 12, 6, 11, 'yen');
INSERT INTO public.moon VALUES (false, 11, 6, 12, 'tam');
INSERT INTO public.moon VALUES (true, 19, 7, 13, 'thu');
INSERT INTO public.moon VALUES (false, 7, 7, 14, 'chien');
INSERT INTO public.moon VALUES (true, 12, 8, 15, 'dai');
INSERT INTO public.moon VALUES (false, 16, 8, 16, 'thang');
INSERT INTO public.moon VALUES (true, 15, 9, 17, 'khai');
INSERT INTO public.moon VALUES (false, 14, 9, 18, 'quynh');
INSERT INTO public.moon VALUES (true, 190, 10, 19, 'dat');
INSERT INTO public.moon VALUES (false, 14, 11, 20, 'dinh');


--
-- Data for Name: planet; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.planet VALUES (13, true, 1, 1, 'earth');
INSERT INTO public.planet VALUES (20, true, 1, 2, 'kepler');
INSERT INTO public.planet VALUES (14, false, 2, 3, 'IC342B');
INSERT INTO public.planet VALUES (19, false, 2, 4, 'IC342C');
INSERT INTO public.planet VALUES (50, false, 3, 5, 'M104B');
INSERT INTO public.planet VALUES (30, false, 3, 6, 'M104C');
INSERT INTO public.planet VALUES (23, false, 4, 7, 'ESO35040B');
INSERT INTO public.planet VALUES (21, false, 4, 8, 'ESO35040C');
INSERT INTO public.planet VALUES (15, false, 5, 9, 'HOB');
INSERT INTO public.planet VALUES (29, false, 5, 10, 'HOC');
INSERT INTO public.planet VALUES (0, false, 6, 11, 'M64B');
INSERT INTO public.planet VALUES (11, false, 6, 12, 'M64C');


--
-- Data for Name: spaceship; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.spaceship VALUES (2, 2004, 1, 'MinhThu');
INSERT INTO public.spaceship VALUES (1, 2023, 2, 'QuocKhanh');
INSERT INTO public.spaceship VALUES (3, 1999, 3, 'YeuNhau');


--
-- Data for Name: star; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.star VALUES (1, 'yello', 2.0000, 1, 'sun');
INSERT INTO public.star VALUES (2, 'red', 1.0000, 2, 'thu');
INSERT INTO public.star VALUES (3, 'yellow', 1.0000, 3, 'bong');
INSERT INTO public.star VALUES (4, 'red', 3.0000, 4, 'hoag');
INSERT INTO public.star VALUES (5, 'white', 2.0000, 5, 'cart');
INSERT INTO public.star VALUES (6, 'yellow', 6.0000, 6, 'eye');


--
-- Name: galaxy galaxy_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_name_key UNIQUE (name);


--
-- Name: galaxy galaxy_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_pkey PRIMARY KEY (galaxy_id);


--
-- Name: galaxy galaxy_unq; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_unq UNIQUE (galaxy_id);


--
-- Name: moon moon_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_pkey PRIMARY KEY (moon_id);


--
-- Name: moon moon_unq; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_unq UNIQUE (moon_id);


--
-- Name: planet planet_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_pkey PRIMARY KEY (planet_id);


--
-- Name: planet planet_unq; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_unq UNIQUE (planet_id);


--
-- Name: spaceship spaceship_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.spaceship
    ADD CONSTRAINT spaceship_name_key UNIQUE (name);


--
-- Name: spaceship spaceship_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.spaceship
    ADD CONSTRAINT spaceship_pkey PRIMARY KEY (spaceship_id);


--
-- Name: spaceship spaceship_year_launched_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.spaceship
    ADD CONSTRAINT spaceship_year_launched_key UNIQUE (year_launched);


--
-- Name: star star_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_name_key UNIQUE (name);


--
-- Name: star star_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_pkey PRIMARY KEY (star_id);


--
-- Name: spaceship spaceship_planet_visited_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.spaceship
    ADD CONSTRAINT spaceship_planet_visited_id_fkey FOREIGN KEY (planet_visited_id) REFERENCES public.planet(planet_id);


--
-- Name: star star_galaxy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_galaxy_id_fkey FOREIGN KEY (galaxy_id) REFERENCES public.galaxy(galaxy_id);


--
-- PostgreSQL database dump complete
--

