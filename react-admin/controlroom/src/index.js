import React from 'react';
import ReactDOM from 'react-dom';
import { Admin, Resource } from 'react-admin';
import jsonRestProvider from 'ra-data-fakerest';

import data from './data';
// import posts from './posts';
import service_pages from './service_pages';
import topics from './topics';
// import comments from './comments';

import './styles.css';

const disableFakeFetchRequestsLogs = true;
const App = () => (
  <Admin dataProvider={jsonRestProvider(data, disableFakeFetchRequestsLogs)}>
    <Resource name="service_pages" {...service_pages} />
    {/* <Resource name="posts" {...posts} /> */}
    <Resource name="topics" {...topics} />
    <Resource name="tags" />
  </Admin>
);

const rootElement = document.getElementById('root');
ReactDOM.render(<App />, rootElement);
