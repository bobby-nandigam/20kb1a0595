import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { Card, CardContent, CardMedia, Typography } from '@mui/material';

const ProductDetailPage = () => {
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    fetchProduct();
  }, [id]);

  const fetchProduct = async () => {
    try {
      const response = await axios.get(`YOUR_BACKEND_API/products/${id}`);
      setProduct(response.data);
    } catch (error) {
      console.error('Error fetching product:', error);
    }
  };

  if (!product) return <div>Loading...</div>;

  return (
    <Card>
      <CardMedia component="img" image="RANDOM_IMAGE_URL" alt={product.name} />
      <CardContent>
        <Typography variant="h5">{product.name}</Typography>
        <Typography variant="subtitle1">{product.company}</Typography>
        <Typography variant="body2">{product.category}</Typography>
        <Typography variant="body1">${product.price}</Typography>
        <Typography variant="body2">Rating: {product.rating}</Typography>
        <Typography variant="body2">Discount: {product.discount}%</Typography>
        <Typography variant="body2">Availability: {product.availability ? 'In stock' : 'Out of stock'}</Typography>
      </CardContent>
    </Card>
  );
};

export default ProductDetailPage;
