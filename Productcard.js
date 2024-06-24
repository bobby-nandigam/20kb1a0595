import React from 'react';
import { Card, CardContent, CardMedia, Typography } from '@mui/material';
import { Link } from 'react-router-dom';

const ProductCard = ({ product }) => {
  return (
    <Card>
      <CardMedia component="img" height="140" image="RANDOM_IMAGE_URL" alt={product.name} />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          <Link to={`/product/${product.id}`}>{product.name}</Link>
        </Typography>
        <Typography variant="body2" color="text.secondary">
          {product.company}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          {product.price} USD
        </Typography>
      </CardContent>
    </Card>
  );
};

export default ProductCard;
