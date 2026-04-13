import React from 'react';
import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
import { store } from './app/store';

import TrainUnitsList from './pages/TrainUnitsList';

ReactDOM.createRoot(document.getElementById('root')).render(
  <Provider store={store}>
    
    <TrainUnitsList />
  </Provider>
);