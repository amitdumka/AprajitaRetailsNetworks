import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Customers.styles';

class Customers extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Customers will mount');
  }

  componentDidMount = () => {
    console.log('Customers mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Customers will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Customers will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Customers did update');
  }

  componentWillUnmount = () => {
    console.log('Customers will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="CustomersWrapper">
        Test content
      </div>
    );
  }
}

Customers.propTypes = {
  // bla: PropTypes.string,
};

Customers.defaultProps = {
  // bla: 'test',
};

const mapStateToProps = state => ({
  // blabla: state.blabla,
});

const mapDispatchToProps = dispatch => ({
  // fnBlaBla: () => dispatch(action.name()),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Customers);
