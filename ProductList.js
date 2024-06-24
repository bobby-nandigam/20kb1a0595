import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Grid, TextField, Select, MenuItem, InputLabel, FormControl, Button } from '@mui/material';
import ProductCard from '../components/ProductCard';

const ProductListPage = () => {
  const [products, setProducts] = useState([]);
  const [filters, setFilters] = useState({
    category: '',
    company: '',
    rating: '',
    minPrice: '',
    maxPrice: '',
    availability: ''
  });

  useEffect(() => {
    fetchProducts();
  }, [filters]);

  const fetchProducts = async () => {
    try {
      const response = await axios.get('YOUR_BACKEND_API/products', { params: filters });
      setProducts(response.data);
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  };

  const handleFilterChange = (e) => {
    setFilters({ ...filters, [e.target.name]: e.target.value });
  };

  return (
    <div>
      <h1>All Products</h1>
      <div style={{ marginBottom: '20px' }}>
        <FormControl fullWidth>
          <InputLabel>Category</InputLabel>
          <Select name="category" value={filters.category} onChange={handleFilterChange}>
            {/* Add category options here */}
            <MenuItem value="Electronics">Electronics</MenuItem>
            <MenuItem value="Fashion">Fashion</MenuItem>
            {/* Other categories */}
          </Select>
        </FormControl>
        {/* Add other filters similarly */}
      </div>
      <Grid container spacing={2}>
        {products.map((product) => (
          <Grid item xs={12} sm={6} md={4} key={product.id}>
            <ProductCard product={product} />
          </Grid>
        ))}
      </Grid>
    </div>
  );
};

export default ProductListPage;
