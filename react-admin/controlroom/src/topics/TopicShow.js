import React from 'react';
import {
  Datagrid,
  DateField,
  ShowButton,
  ReferenceManyField,
  RichTextField,
  Show,
  Tab,
  TabbedShowLayout,
  TextField
} from 'react-admin';
// import AddPageButton from './AddPageButton';

const TopicShow = props => (
  <Show {...props}>
    <TabbedShowLayout>
      <Tab label="Summary">
        <TextField source="id" />
        <TextField source="name" />
      </Tab>
      {/*
      <Tab label="Body" path="body">
        <RichTextField
          source="body"
          stripTags={false}
          label=""
          addLabel={false}
        />
      </Tab>
      */}
      <Tab label="Service Pages" path="service_pages">
        <ReferenceManyField
          addLabel={false}
          reference="service_pages"
          target="topic_id"
        >
          <Datagrid>
            <TextField source="name" />
            <ShowButton />
          </Datagrid>
        </ReferenceManyField>
        {/* <AddCommentButton /> */}
      </Tab>
    </TabbedShowLayout>
  </Show>
);

export default TopicShow;
