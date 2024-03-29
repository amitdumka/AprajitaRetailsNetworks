/**
 * ConfigButton
 *  It show a config Button at the bottom right of the screen
 */

// Aprajita Retails React components
import SoftBox from "components/SoftBox";
import Icon from "@mui/material/Icon";

function ConfigButton() {
    return (
        <SoftBox
          display="flex"
          justifyContent="center"
          alignItems="center"
          width="3.5rem"
          height="3.5rem"
          bgColor="white"
          shadow="sm"
          borderRadius="50%"
          position="fixed"
          right="2rem"
          bottom="2rem"
          zIndex={99}
          color="dark"
          sx={{ cursor: "pointer" }}
          onClick={handleConfiguratorOpen}
        >
          <Icon fontSize="default" color="inherit">
            settings
          </Icon>
        </SoftBox>
      );
}