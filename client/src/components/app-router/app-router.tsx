import React from 'react';

import {createBrowserRouter, RouterProvider } from 'react-router-dom';

import AutocompletePage from '../../pages/autocomplete-page/autocomplete-page';
import FTSEPage from '../../pages/ftse-page';

  
const AppRouter: React.FC = () => {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <AutocompletePage />,
    },
    {
      path: "/ftse",
      element: <FTSEPage />,
    }
  ]);
  
  return (
    <RouterProvider router={router} />
  );
};

export default AppRouter;
