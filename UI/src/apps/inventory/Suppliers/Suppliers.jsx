import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Suppliers.styles';

class Suppliers extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Suppliers will mount');
  }

  componentDidMount = () => {
    console.log('Suppliers mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Suppliers will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Suppliers will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Suppliers did update');
  }

  componentWillUnmount = () => {
    console.log('Suppliers will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="SuppliersWrapper">
        Test content
      </div>
    );
  }
}

Suppliers.propTypes = {
  // bla: PropTypes.string,
};

Suppliers.defaultProps = {
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
)(Suppliers);
