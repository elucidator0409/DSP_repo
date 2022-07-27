import axios from "axios";
import { useEffect, useState } from "react";
import { Row } from "react-bootstrap";
import Message from "../components/Message";
import RelatedMovieCard from "../components/RelatedMovieCard";

const parseQuery = (queryString) => {
  if (queryString.length <= 1) return {
    query: ""
  }

  const queries = queryString.split('&');
  queries[0] = queries[0].slice(1);

  let output = {
    query: ""
  };

  queries.forEach((query) => {
    const set = query.split("=");
    if(set[0] === "query") output = {
      query: set[1]
    }
  });

  return output;
};

const SearchScreen = ({ history }) => {
  const [relatedMoviesIds, setRelatedMoviesIds] = useState([]);
  const [err, setErr] = useState("");
  const query = parseQuery(history.location.search);

  useEffect(() => {
    const getRelatedMovies = async () => {
      try {
        const { data } = await axios.get('https://54ax7f00b7.execute-api.us-east-1.amazonaws.com/default/movieRecommderInvocation', {
          params: {
            query: query.query
          }
        });

        setRelatedMoviesIds(data.ids);
      } catch (error) {
        setErr(error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message);
      }
    }

    getRelatedMovies();
  }, [query.query])

  return(
    <div>
      <h2>Search result for "{decodeURI(query.query)}"</h2>
      { err ? <Message variant="danger">could not query model!</Message> 
      : 
        <Row>
        {
          relatedMoviesIds.map((movieId, index) => {
            return <RelatedMovieCard key={index} movieId={movieId} />;
          })
        }
        </Row>
      }
    </div>
  );
}

export default SearchScreen;