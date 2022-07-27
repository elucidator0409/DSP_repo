import Message from "./Message";
import Loader from '../components/Loader';
import Product from "./Product";
import useGetMovieById from "../hooks/useGetMovieById";
import { Card, Col } from "react-bootstrap";

const RelatedMovieCard = ({ movieId }) => {
  const { loading, error, movie } = useGetMovieById(movieId);

  if (loading) return (
    <Card>
      <Card.Body>
          <Loader />
      </Card.Body>
    </Card>
  )

  if (error) {
    console.log('errormsg', error);
    return (
      <Message variant="danger">Movie does not exist for id {movieId}</Message>
    );
  }

  return (
    <Col key={movie.id} sm={12} md={6} lg={4} xl={3}>
      <Product product={movie} />
    </Col>
  );
}

export default RelatedMovieCard;