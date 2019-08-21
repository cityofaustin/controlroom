import React from 'react';
import { ReferenceField, Show, SimpleShowLayout, TextField } from 'react-admin';

const ServicePageShow = props => (
  <Show {...props}>
    <SimpleShowLayout>
      <TextField source="id" />
      <TextField source="name" />
      <ReferenceField source="topic_id" reference="topics">
        <TextField source="name" />
      </ReferenceField>
    </SimpleShowLayout>
  </Show>
);

export default ServicePageShow;
