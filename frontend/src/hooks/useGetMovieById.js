import axios from "axios";
import { useEffect, useState } from "react"

const useGetMovieById = (movieId) => {
  const [loading, setLoading] = useState(false);
  const [movie, setMovie] = useState({});
  const [error, setError] = useState("");

  useEffect(() => {
    const getMovieById = async () => {
      setError("");
      setLoading(true);

      try {
        const { data } = await axios.get(`/api/products/${movieId}`);

        setMovie(data);
        setLoading(false);
      } catch (error) {
        setLoading(false);
        setError(error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message);
      }
    }

    getMovieById();
  }, [movieId]);

  return {
    loading, error, movie
  }
}

export default useGetMovieById;