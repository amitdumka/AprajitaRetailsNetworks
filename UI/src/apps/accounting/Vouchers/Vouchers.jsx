import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Vouchers.styles';

class Vouchers extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Vouchers will mount');
  }

  componentDidMount = () => {
    console.log('Vouchers mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Vouchers will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Vouchers will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Vouchers did update');
  }

  componentWillUnmount = () => {
    console.log('Vouchers will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="VouchersWrapper">
        Test content
      </div>
    );
  }
}

Vouchers.propTypes = {
  // bla: PropTypes.string,
};

Vouchers.defaultProps = {
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
)(Vouchers);
