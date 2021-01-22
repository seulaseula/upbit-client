/*
 * Upbit Open API
 * ## REST API for Upbit Exchange - Base URL: [https://api.upbit.com] - Official Upbit API Documents: [https://docs.upbit.com] - Official Support email: [open-api@upbit.com] 
 *
 * OpenAPI spec version: 1.0.0
 * Contact: ujhin942@gmail.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * APIKey
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2021-01-22T16:02:42.285Z")
public class APIKey {
  @SerializedName("access_key")
  private String accessKey = null;

  @SerializedName("expire_at")
  private String expireAt = null;

  public APIKey accessKey(String accessKey) {
    this.accessKey = accessKey;
    return this;
  }

   /**
   * Get accessKey
   * @return accessKey
  **/
  @ApiModelProperty(example = "xxxxxxxxxxxxxxxxxxxxxxxx", value = "")
  public String getAccessKey() {
    return accessKey;
  }

  public void setAccessKey(String accessKey) {
    this.accessKey = accessKey;
  }

  public APIKey expireAt(String expireAt) {
    this.expireAt = expireAt;
    return this;
  }

   /**
   * Get expireAt
   * @return expireAt
  **/
  @ApiModelProperty(example = "", value = "")
  public String getExpireAt() {
    return expireAt;
  }

  public void setExpireAt(String expireAt) {
    this.expireAt = expireAt;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    APIKey apIKey = (APIKey) o;
    return Objects.equals(this.accessKey, apIKey.accessKey) &&
        Objects.equals(this.expireAt, apIKey.expireAt);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accessKey, expireAt);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class APIKey {\n");
    
    sb.append("    accessKey: ").append(toIndentedString(accessKey)).append("\n");
    sb.append("    expireAt: ").append(toIndentedString(expireAt)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
