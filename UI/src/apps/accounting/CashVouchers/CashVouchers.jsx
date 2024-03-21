import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './CashVouchers.styles';

class CashVouchers extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('CashVouchers will mount');
  }

  componentDidMount = () => {
    console.log('CashVouchers mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('CashVouchers will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('CashVouchers will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('CashVouchers did update');
  }

  componentWillUnmount = () => {
    console.log('CashVouchers will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="CashVouchersWrapper">
        Test content
      </div>
    );
  }
}

CashVouchers.propTypes = {
  // bla: PropTypes.string,
};

CashVouchers.defaultProps = {
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
)(CashVouchers);
