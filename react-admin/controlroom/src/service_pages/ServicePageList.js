import { withStyles } from '@material-ui/core/styles';
import React from 'react';
import {
  Datagrid,
  List,
  Responsive,
  ShowButton,
  SimpleList,
  TextField
} from 'react-admin';

const styles = theme => ({
  title: {
    maxWidth: '20em',
    overflow: 'hidden',
    textOverflow: 'ellipsis',
    whiteSpace: 'nowrap'
  }
});

const ServicePageList = withStyles(styles)(({ classes, ...props }) => (
  <List {...props}>
    <Responsive
      small={<SimpleList linkType="show" primaryText={record => record.name} />}
      medium={
        <Datagrid>
          <TextField source="id" />
          <TextField source="name" />
          <ShowButton />
        </Datagrid>
      }
    />
  </List>
));

export default ServicePageList;
