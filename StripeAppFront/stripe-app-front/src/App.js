import React from 'react';
import './App.css';
import {
  Elements,
} from '@stripe/react-stripe-js';

import {loadStripe} from "@stripe/stripe-js/pure";
import CheckoutForm from "./components/CheckoutForm";

const stripePromise = loadStripe('pk_test_51HxEBgBt936UMiAMQkOnjrNLMNEOuwm9Yyfn5RrRaqYjXwnAbPdgOxYSi9HI3XQmnsycmeQqEeQiCpeww978GIqi002VqjHJaH');


const App = () => (
    <Elements stripe={stripePromise}>
      <CheckoutForm />
    </Elements>
);

export default App;